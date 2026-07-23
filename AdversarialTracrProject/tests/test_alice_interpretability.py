import unittest

import torch

from src.alice import AliceNet, train_anc
from src.alice_interpretability import probe_position
from src.bob import BobNet
from src.eve import EveNet


class AliceInterpretabilityTest(unittest.TestCase):
    def test_hidden_layer_probe_beats_raw_input_baseline(self) -> None:
        torch.manual_seed(0)
        msg_length = 4
        alice = AliceNet(msg_length=msg_length)
        bob = BobNet(msg_length=msg_length)
        eve = EveNet(msg_length=msg_length)

        train_anc(
            alice,
            bob,
            eve,
            train_steps=500,
            minibatch_size=64,
            lr=1e-3,
            msg_length=msg_length,
            alpha=1.0,
            beta=1.0,
            log_every=500,
        )

        input_result = probe_position(
            alice, msg_length, position=0, source="input", n_train=1024, n_test=256, steps=200
        )
        hidden_result = probe_position(
            alice, msg_length, position=0, source="hidden", n_train=1024, n_test=256, steps=200
        )

        # XOR no es linealmente separable en (msg_i, key_i): el baseline sobre
        # input crudo no puede superar el límite teórico de una única frontera
        # lineal (3 de 4 combinaciones, 75%).
        self.assertLessEqual(input_result.test_acc, 0.85)
        # Si Alice aprendió una representación útil, la capa oculta post-ReLU
        # debería hacer que el bit XOR sea linealmente legible con clara ventaja
        # sobre el baseline no lineal-separable.
        self.assertGreater(hidden_result.test_acc, input_result.test_acc)


if __name__ == "__main__":
    unittest.main()
