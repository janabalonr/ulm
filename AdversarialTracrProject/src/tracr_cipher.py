"""Cifrado XOR explícito codificado en RASP y compilado con Tracr.

Sirve como referencia de verdad (ground truth) interpretativa para contrastar
con el cifrado emergente que aprende `AliceNet` (ver `src/alice.py`).

Codificación de entrada: una única secuencia de largo `2*msg_length`, donde
las posiciones `[0, msg_length)` contienen los bits del mensaje y las
posiciones `[msg_length, 2*msg_length)` contienen los bits de la clave. La
salida en la posición `i` (para `i < msg_length`) es `msg[i] XOR key[i]`.
"""

from typing import Sequence

from tracr.compiler import compiling
from tracr.compiler.assemble import AssembledTransformerModel
from tracr.rasp import rasp


def build_xor_program(msg_length: int) -> rasp.SOp:
    """Construye el programa RASP que calcula el XOR bit a bit de msg y key."""
    select_key_bit = rasp.Select(
        rasp.indices,
        rasp.indices,
        lambda key_pos, query_pos: key_pos == query_pos + msg_length,
    )
    key_echo = rasp.Aggregate(select_key_bit, rasp.tokens, default=None)
    return rasp.SequenceMap(
        lambda msg_bit, key_bit: msg_bit ^ key_bit if key_bit is not None else msg_bit,
        rasp.tokens,
        key_echo,
    )


def build_input_sequence(msg_bits: Sequence[int], key_bits: Sequence[int]) -> list[int]:
    if len(msg_bits) != len(key_bits):
        raise ValueError(
            f"msg_bits y key_bits deben tener el mismo largo, se recibió {len(msg_bits)} y {len(key_bits)}"
        )
    return list(msg_bits) + list(key_bits)


def eval_xor_rasp(msg_bits: Sequence[int], key_bits: Sequence[int]) -> list[int]:
    """Evalúa el programa RASP de forma simbólica, sin compilar un transformer."""
    program = build_xor_program(len(msg_bits))
    seq = build_input_sequence(msg_bits, key_bits)
    out = rasp.evaluate(program, seq)
    return list(out[: len(msg_bits)])


def compile_xor_model(msg_length: int, compiler_bos: str = "BOS") -> AssembledTransformerModel:
    """Compila el programa RASP a un transformer explícito (pesos y estructura conocidos)."""
    program = build_xor_program(msg_length)
    return compiling.compile_rasp_to_model(
        program,
        vocab={0, 1},
        max_seq_len=2 * msg_length,
        compiler_bos=compiler_bos,
    )


def eval_xor_model(
    model: AssembledTransformerModel,
    msg_bits: Sequence[int],
    key_bits: Sequence[int],
    compiler_bos: str = "BOS",
) -> list[int]:
    """Corre el transformer compilado y devuelve los bits de salida decodificados."""
    seq = build_input_sequence(msg_bits, key_bits)
    out = model.apply([compiler_bos] + seq)
    return list(out.decoded[1 : 1 + len(msg_bits)])


if __name__ == "__main__":
    msg_length = 4
    msg = [1, 0, 1, 1]
    key = [0, 1, 1, 0]

    rasp_out = eval_xor_rasp(msg, key)
    print("XOR (evaluación simbólica RASP):", rasp_out)

    model = compile_xor_model(msg_length)
    model_out = eval_xor_model(model, msg, key)
    print("XOR (transformer compilado con Tracr):", model_out)
