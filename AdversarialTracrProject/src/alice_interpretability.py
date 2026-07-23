"""Sonda lineal sobre las activaciones ocultas de AliceNet.

Complementa `interpretability.py` (que lee la estructura del transformer
compilado con Tracr, conocida por construcción) usando el mismo vocabulario de
variables -- el bit de clave por posición y el bit de salida XOR por posición
(`aggregate_2` / `sequence_map_1` en Tracr) -- como hipótesis a verificar
dentro de una red opaca (AliceNet).

A diferencia de Tracr, donde esas variables son dimensiones one-hot legibles
al 100% por construcción, acá no sabemos de antemano si están codificadas ni
cómo. Se entrena una sonda lineal (regresión logística) que intenta predecir
el bit XOR de salida en una posición dada a partir de las activaciones de
Alice, y se compara contra un baseline sobre el input crudo: como XOR no es
linealmente separable en las dos variables relevantes (msg_i, key_i), ese
baseline funciona como control de que la sonda depende de la representación
aprendida por Alice y no de una trivialidad del input.
"""

import dataclasses

import torch
import torch.nn as nn

try:
    from .alice import AliceNet, explicit_xor_cipher, generate_data
except ImportError:  # pragma: no cover - allows running the script directly
    from alice import AliceNet, explicit_xor_cipher, generate_data


def hidden_activations(alice: AliceNet, msg: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
    """Activaciones post-ReLU de la capa oculta fc1 de Alice."""
    x = torch.cat([msg, key], dim=1)
    return torch.relu(alice.fc1(x))


@dataclasses.dataclass
class ProbeResult:
    position: int
    source: str
    train_acc: float
    test_acc: float


def _train_linear_probe(features: torch.Tensor, labels: torch.Tensor, steps: int, lr: float) -> nn.Linear:
    probe = nn.Linear(features.shape[1], 1)
    optimizer = torch.optim.Adam(probe.parameters(), lr=lr)
    bce = nn.BCEWithLogitsLoss()
    for _ in range(steps):
        optimizer.zero_grad()
        loss = bce(probe(features).squeeze(-1), labels)
        loss.backward()
        optimizer.step()
    return probe


def _accuracy(probe: nn.Linear, features: torch.Tensor, labels: torch.Tensor) -> float:
    with torch.no_grad():
        preds = (torch.sigmoid(probe(features).squeeze(-1)) > 0.5).float()
        return (preds == labels).float().mean().item()


def probe_position(
    alice: AliceNet,
    msg_length: int,
    position: int,
    source: str = "hidden",
    n_train: int = 4096,
    n_test: int = 1024,
    steps: int = 500,
    lr: float = 0.1,
) -> ProbeResult:
    """Entrena una sonda lineal para leer el bit XOR de salida en `position`.

    `source="hidden"` usa la capa oculta post-ReLU de Alice. `source="input"`
    usa msg+key crudos como baseline no lineal-separable.
    """
    msg_train, key_train = generate_data(n_train, msg_length)
    msg_test, key_test = generate_data(n_test, msg_length)

    xor_train = explicit_xor_cipher(msg_train, key_train)[:, position]
    xor_test = explicit_xor_cipher(msg_test, key_test)[:, position]

    if source == "hidden":
        feats_train = hidden_activations(alice, msg_train, key_train).detach()
        feats_test = hidden_activations(alice, msg_test, key_test).detach()
    elif source == "input":
        feats_train = torch.cat([msg_train, key_train], dim=1)
        feats_test = torch.cat([msg_test, key_test], dim=1)
    else:
        raise ValueError(f"source desconocido: {source!r}, use 'hidden' o 'input'")

    probe = _train_linear_probe(feats_train, xor_train, steps=steps, lr=lr)
    return ProbeResult(
        position=position,
        source=source,
        train_acc=_accuracy(probe, feats_train, xor_train),
        test_acc=_accuracy(probe, feats_test, xor_test),
    )


def probe_all_positions(
    alice: AliceNet,
    msg_length: int,
    source: str = "hidden",
    **kwargs,
) -> list[ProbeResult]:
    return [probe_position(alice, msg_length, i, source=source, **kwargs) for i in range(msg_length)]


if __name__ == "__main__":
    from alice import train_anc
    from bob import BobNet
    from eve import EveNet

    torch.manual_seed(0)

    N = 8
    alice = AliceNet(msg_length=N)
    bob = BobNet(msg_length=N)
    eve = EveNet(msg_length=N)

    print("Entrenando ANC...")
    train_anc(alice, bob, eve, train_steps=2000, minibatch_size=128, msg_length=N, log_every=500)

    print("\nSonda lineal -- baseline sobre input crudo (XOR no es linealmente separable):")
    for r in probe_all_positions(alice, N, source="input"):
        print(f"  pos={r.position}: train_acc={r.train_acc:.3f} test_acc={r.test_acc:.3f}")

    print("\nSonda lineal -- capa oculta de Alice (post-ReLU):")
    for r in probe_all_positions(alice, N, source="hidden"):
        print(f"  pos={r.position}: train_acc={r.train_acc:.3f} test_acc={r.test_acc:.3f}")
