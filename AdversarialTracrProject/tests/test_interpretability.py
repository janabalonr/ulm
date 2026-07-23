import unittest

from src.interpretability import (
    describe_trace,
    get_variable_value,
    run_with_trace,
    verify_key_offset_attention,
)
from src.tracr_cipher import compile_xor_model


class InterpretabilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.msg_length = 4
        cls.model = compile_xor_model(cls.msg_length)

    def test_attention_learns_key_offset(self) -> None:
        self.assertTrue(verify_key_offset_attention(self.model, self.msg_length))

    def test_residual_trace_matches_expected_xor(self) -> None:
        msg, key = [1, 0, 1, 1], [0, 1, 1, 0]
        trace = run_with_trace(self.model, msg, key)

        for i in range(1, self.msg_length + 1):
            msg_bit = get_variable_value(trace, "tokens", i)
            key_bit = get_variable_value(trace, "aggregate_2", i)
            xor_bit = get_variable_value(trace, "sequence_map_1", i)

            self.assertEqual(msg_bit, msg[i - 1])
            self.assertEqual(key_bit, key[i - 1])
            self.assertEqual(xor_bit, msg[i - 1] ^ key[i - 1])

    def test_describe_trace_is_readable(self) -> None:
        msg, key = [0, 1, 0, 1], [1, 1, 0, 0]
        trace = run_with_trace(self.model, msg, key)
        text = describe_trace(trace, self.msg_length)

        self.assertEqual(len(text.splitlines()), self.msg_length)
        self.assertIn("xor_out=1", text)


if __name__ == "__main__":
    unittest.main()
