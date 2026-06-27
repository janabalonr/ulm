import torch
import torch.nn as nn

try:
    from .bob import BobNet
    from .eve import EveNet
except ImportError:  # pragma: no cover - allows running the script directly
    from bob import BobNet
    from eve import EveNet


class AliceNet(nn.Module):
    """Alice network para adversarial neural cryptography (Abadi-style)."""

    def __init__(self, msg_length: int):
        super().__init__()
        self.msg_length = msg_length
        self.input_length = 2 * msg_length

        self.fc1 = nn.Linear(self.input_length, self.input_length)
        self.fc2 = nn.Linear(self.input_length, self.msg_length)
        self._initialize_weights()

    def _initialize_weights(self) -> None:
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.zeros_(self.fc1.bias)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.zeros_(self.fc2.bias)

    def forward(self, msg: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        """Produce a ciphertext from message and shared key."""
        if msg.shape[1] != self.msg_length or key.shape[1] != self.msg_length:
            raise ValueError(
                f"msg and key must have length {self.msg_length}, "
                f"got {msg.shape[1]} and {key.shape[1]}"
            )

        x = torch.cat([msg, key], dim=1)
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x


def explicit_xor_cipher(msg: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
    """Devuelve el cifrado explícito de XOR bit a bit para compararlo con el cifrado ANC aprendido."""
    if msg.shape != key.shape:
        raise ValueError(f"msg and key must have the same shape, got {msg.shape} and {key.shape}")
    return torch.logical_xor(msg.bool(), key.bool()).float()


def compare_ciphertext_to_xor(ciphertext: torch.Tensor, msg: torch.Tensor, key: torch.Tensor) -> tuple[float, float]:
    """Compara el texto cifrado ANC aprendido con la referencia explícita de XOR"""
    xor_target = explicit_xor_cipher(msg, key)
    binary_cipher = (ciphertext >= 0.5).float()
    match_rate = ((binary_cipher == xor_target).float().mean().item())
    error = (binary_cipher - xor_target).abs().mean().item()
    return match_rate, error


def generate_data(batch_size: int, msg_length: int) -> tuple[torch.Tensor, torch.Tensor]:
    msg = torch.randint(0, 2, (batch_size, msg_length), dtype=torch.float32)
    key = torch.randint(0, 2, (batch_size, msg_length), dtype=torch.float32)
    return msg, key


def train_anc(
    alice: AliceNet,
    bob: BobNet,
    eve: EveNet,
    train_steps: int = 15000,
    minibatch_size: int = 4096,
    lr: float = 1e-3,
    msg_length: int = 16,
    alpha: float = 1.0,
    beta: float = 0.5,
    eve_updates_per_round: int = 2,
    log_every: int = 1000,
    epochs: int | None = None,
    batch_size: int | None = None,
) -> None:
    if epochs is not None:
        train_steps = epochs
    if batch_size is not None:
        minibatch_size = batch_size

    optimizer_alice = torch.optim.Adam(alice.parameters(), lr=lr)
    optimizer_bob = torch.optim.Adam(bob.parameters(), lr=lr)
    optimizer_eve = torch.optim.Adam(eve.parameters(), lr=lr)
    bce = nn.BCELoss()

    for step in range(1, train_steps + 1):
        msg, key = generate_data(minibatch_size, msg_length)
        xor_target = explicit_xor_cipher(msg, key)

        ciphertext = alice(msg, key)
        bob_pred = bob(ciphertext, key)
        eve_pred = eve(ciphertext)
        bob_loss = bce(bob_pred, msg)
        eve_loss = bce(eve_pred, msg)

        optimizer_bob.zero_grad()
        bob_loss.backward(retain_graph=True)
        optimizer_bob.step()

        ciphertext = alice(msg, key)
        bob_pred = bob(ciphertext, key)
        eve_pred = eve(ciphertext)
        bob_loss = bce(bob_pred, msg)
        eve_loss = bce(eve_pred, msg)
        xor_loss = bce(ciphertext, xor_target)

        optimizer_alice.zero_grad()
        alice_loss = bob_loss - alpha * eve_loss + beta * xor_loss
        alice_loss.backward()
        optimizer_alice.step()

        for _ in range(eve_updates_per_round):
            eve_msg, eve_key = generate_data(minibatch_size, msg_length)
            eve_ciphertext = alice(eve_msg, eve_key)
            eve_pred = eve(eve_ciphertext)
            eve_loss = bce(eve_pred, eve_msg)

            optimizer_eve.zero_grad()
            eve_loss.backward()
            optimizer_eve.step()

        if step % log_every == 0 or step == 1:
            msg_eval, key_eval = generate_data(minibatch_size, msg_length)
            ciphertext_eval = alice(msg_eval, key_eval)
            bob_pred_eval = bob(ciphertext_eval, key_eval)
            eve_pred_eval = eve(ciphertext_eval)
            bob_acc = ((bob_pred_eval > 0.5).float() == msg_eval).float().mean().item()
            eve_acc = ((eve_pred_eval > 0.5).float() == msg_eval).float().mean().item()
            xor_match, xor_error = compare_ciphertext_to_xor(ciphertext_eval, msg_eval, key_eval)
            print(
                f"Step {step}/{train_steps} - bob_acc={bob_acc:.3f} "
                f"eve_acc={eve_acc:.3f} xor_match={xor_match:.3f} xor_error={xor_error:.3f}"
            )


if __name__ == "__main__":
    torch.manual_seed(0)

    N = 16
    batch_size = 64

    alice = AliceNet(msg_length=N)
    bob = BobNet(msg_length=N)
    eve = EveNet(msg_length=N)

    print("Entrenando ANC con Alice, Bob y Eve siguiendo la idea de Abadi...")
    train_anc(
        alice,
        bob,
        eve,
        train_steps=2000,
        minibatch_size=128,
        lr=1e-3,
        msg_length=N,
        log_every=200,
    )

    msg, key = generate_data(batch_size=batch_size, msg_length=N)
    ciphertext = alice(msg, key)
    bob_pred = bob(ciphertext, key)
    eve_pred = eve(ciphertext)

    bob_acc = ((bob_pred > 0.5).float() == msg).float().mean().item()
    eve_acc = ((eve_pred > 0.5).float() == msg).float().mean().item()
    xor_match, xor_error = compare_ciphertext_to_xor(ciphertext, msg, key)

    print("msg shape:", msg.shape)
    print("key shape:", key.shape)
    print("ciphertext shape:", ciphertext.shape)
    print("bob accuracy:", bob_acc)
    print("eve accuracy:", eve_acc)
    print("xor match rate:", xor_match)
    print("xor error:", xor_error)
