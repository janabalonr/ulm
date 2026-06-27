import unittest

import torch

from src.alice import AliceNet, compare_ciphertext_to_xor, explicit_xor_cipher, generate_data, train_anc
from src.bob import BobNet
from src.eve import EveNet


class AncTrainingTest(unittest.TestCase):
    def test_explicit_xor_matches_reference(self) -> None:
        msg = torch.tensor([[0, 1, 1, 0]], dtype=torch.float32)
        key = torch.tensor([[1, 1, 0, 0]], dtype=torch.float32)

        expected = torch.tensor([[1, 0, 1, 0]], dtype=torch.float32)
        actual = explicit_xor_cipher(msg, key)

        self.assertTrue(torch.equal(actual, expected))

    def test_training_produces_bob_superiority(self) -> None:
        torch.manual_seed(0)
        alice = AliceNet(msg_length=8)
        bob = BobNet(msg_length=8)
        eve = EveNet(msg_length=8)

        train_anc(
            alice,
            bob,
            eve,
            train_steps=200,
            minibatch_size=32,
            lr=1e-3,
            msg_length=8,
            alpha=1.0,
            beta=1.0,
            log_every=100,
        )

        msg, key = generate_data(batch_size=16, msg_length=8)
        ciphertext = alice(msg, key)
        bob_pred = bob(ciphertext, key)
        eve_pred = eve(ciphertext)

        bob_acc = ((bob_pred > 0.5).float() == msg).float().mean().item()
        eve_acc = ((eve_pred > 0.5).float() == msg).float().mean().item()
        xor_match, xor_error = compare_ciphertext_to_xor(ciphertext, msg, key)

        self.assertEqual(ciphertext.shape, (16, 8))
        self.assertGreater(bob_acc, 0.5)
        self.assertLess(eve_acc, bob_acc + 0.1)
        self.assertGreater(xor_match, 0.45)
        self.assertLess(xor_error, 0.6)


if __name__ == "__main__":
    unittest.main()
