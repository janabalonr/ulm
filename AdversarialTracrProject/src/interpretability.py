"""Herramientas para inspeccionar la estructura interna del transformer XOR
compilado con Tracr (`src/tracr_cipher.py`).

A diferencia de `AliceNet` (una MLP opaca cuyo cifrado emerge del
entrenamiento), el modelo compilado tiene una estructura *conocida por
construcción*: cada dimensión del residual stream corresponde a una variable
RASP concreta (ver `model.residual_labels`), y el patrón de atención se puede
leer directamente para verificar cómo fluye la información del bit de clave
hacia el bit de mensaje correspondiente. Este módulo expone esa estructura de
forma legible para usarla como referencia de verdad interpretativa.
"""

import dataclasses
from typing import Optional, Sequence, Union

import numpy as np
from tracr.compiler.assemble import AssembledTransformerModel

try:
    from .tracr_cipher import build_input_sequence
except ImportError:  # pragma: no cover - allows running the script directly
    from tracr_cipher import build_input_sequence


@dataclasses.dataclass
class Trace:
    """Traza completa de una pasada hacia adelante del modelo compilado."""

    tokens: list
    decoded: list
    residual_labels: list[str]
    residuals: np.ndarray  # (sublayer, posición, dim), batch ya descartado
    attn: np.ndarray  # (posición_query, posición_key), única capa/cabeza


def run_with_trace(
    model: AssembledTransformerModel,
    msg_bits: Sequence[int],
    key_bits: Sequence[int],
    compiler_bos: str = "BOS",
) -> Trace:
    """Corre el modelo y extrae residual stream + patrón de atención con etiquetas."""
    tokens = [compiler_bos] + build_input_sequence(msg_bits, key_bits)
    out = model.apply(tokens)
    residuals = np.asarray(out.residuals)[:, 0, :, :]
    attn = np.asarray(out.attn_logits)[0, 0, 0]
    return Trace(
        tokens=tokens,
        decoded=list(out.decoded),
        residual_labels=list(model.residual_labels),
        residuals=residuals,
        attn=attn,
    )


def get_variable_value(
    trace: Trace, var_name: str, position: int, sublayer: int = -1
) -> Optional[Union[int, str]]:
    """Decodifica el valor categórico de una variable RASP (p.ej. 'aggregate_2',
    'sequence_map_1', 'tokens') en una posición dada, leyendo las dimensiones
    one-hot `{var_name}:<valor>` del residual stream. Devuelve None si la
    variable no tiene un valor activo en esa posición (p.ej. default=None)."""
    prefix = var_name + ":"
    row = trace.residuals[sublayer, position]
    for i, label in enumerate(trace.residual_labels):
        if label.startswith(prefix) and abs(row[i]) > 0.5:
            suffix = label[len(prefix) :]
            return int(suffix) if suffix.lstrip("-").isdigit() else suffix
    return None


def attended_position(trace: Trace, query_position: int) -> int:
    """Devuelve la posición de la secuencia a la que más atiende `query_position`."""
    return int(np.argmax(trace.attn[query_position]))


def verify_key_offset_attention(
    model: AssembledTransformerModel, msg_length: int, compiler_bos: str = "BOS"
) -> bool:
    """Verifica que la atención aprendida efectivamente conecta cada posición de
    mensaje `i` (1..msg_length, con offset +1 por el BOS) con su bit de clave
    correspondiente `i + msg_length`, tal como se diseñó en `build_xor_program`."""
    msg_bits = [0] * msg_length
    key_bits = [1] * msg_length
    trace = run_with_trace(model, msg_bits, key_bits, compiler_bos)
    return all(
        attended_position(trace, i) == i + msg_length for i in range(1, msg_length + 1)
    )


def describe_trace(trace: Trace, msg_length: int) -> str:
    """Genera una traza legible: para cada bit de mensaje, a qué posición
    atendió, qué bit de clave trajo, y qué bit de salida calculó."""
    lines = []
    for pos in range(1, msg_length + 1):
        msg_bit = get_variable_value(trace, "tokens", pos)
        key_pos = attended_position(trace, pos)
        key_bit = get_variable_value(trace, "aggregate_2", pos)
        xor_bit = get_variable_value(trace, "sequence_map_1", pos)
        lines.append(
            f"pos={pos}: msg_bit={msg_bit}  <-- atiende pos={key_pos} (key_bit={key_bit})  "
            f"==> xor_out={xor_bit}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    from tracr_cipher import compile_xor_model

    msg_length = 4
    model = compile_xor_model(msg_length)

    print("¿Atención = offset +N verificado?:", verify_key_offset_attention(model, msg_length))
    print()

    msg, key = [1, 0, 1, 1], [0, 1, 1, 0]
    trace = run_with_trace(model, msg, key)
    print(f"msg={msg} key={key}")
    print(describe_trace(trace, msg_length))
