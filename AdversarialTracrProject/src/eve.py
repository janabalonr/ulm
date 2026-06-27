import torch
import torch.nn as nn


class EveNet(nn.Module):
    """Eve eavesdropper usado en Abadi-style adversarial neural cryptography."""

    def __init__(self, msg_length: int):
        super().__init__()
        self.msg_length = msg_length

        self.fc1 = nn.Linear(self.msg_length, self.msg_length)
        self.fc2 = nn.Linear(self.msg_length, self.msg_length)
        self._initialize_weights()

    def _initialize_weights(self) -> None:
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.zeros_(self.fc1.bias)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.zeros_(self.fc2.bias)

    def forward(self, ciphertext: torch.Tensor) -> torch.Tensor:
        x = torch.relu(self.fc1(ciphertext))
        x = torch.sigmoid(self.fc2(x))
        return x
