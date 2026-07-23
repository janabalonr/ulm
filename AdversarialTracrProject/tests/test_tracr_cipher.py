import itertools
import unittest

import torch

from src.alice import explicit_xor_cipher
from src.tracr_cipher import compile_xor_model, eval_xor_model, eval_xor_rasp


class TracrXorCipherTest(unittest.TestCase):
    def test_rasp_eval_matches_explicit_xor_reference(self) -> None:
        msg_length = 3
        for msg_bits in itertools.product([0, 1], repeat=msg_length):
            for key_bits in itertools.product([0, 1], repeat=msg_length):
                expected = explicit_xor_cipher(
                    torch.tensor([msg_bits], dtype=torch.float32),
                    torch.tensor([key_bits], dtype=torch.float32),
                )[0].int().tolist()
                actual = eval_xor_rasp(list(msg_bits), list(key_bits))
                self.assertEqual(actual, expected, msg=f"msg={msg_bits} key={key_bits}")

    def test_compiled_model_matches_rasp_eval(self) -> None:
        msg_length = 4
        model = compile_xor_model(msg_length)

        for msg_bits in itertools.product([0, 1], repeat=msg_length):
            for key_bits in itertools.product([0, 1], repeat=msg_length):
                expected = eval_xor_rasp(list(msg_bits), list(key_bits))
                actual = eval_xor_model(model, list(msg_bits), list(key_bits))
                self.assertEqual(actual, expected, msg=f"msg={msg_bits} key={key_bits}")


if __name__ == "__main__":
    unittest.main()
