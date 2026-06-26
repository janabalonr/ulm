import torch
import torch.nn as nn
import torch.nn.functional as F


class AliceNet(nn.Module):
    """Alice network for adversarial cryptography in PyTorch."""

    def __init__(self, msg_length: int):
        super().__init__()
        self.msg_length = msg_length
        self.input_length = 2 * msg_length

        self.fc = nn.Linear(self.input_length, self.input_length)
        # Arquitectura original de Alice: el primer conv1d reduce la longitud de 2N a 2N-3.
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=2, kernel_size=4, stride=1, padding=0)
        self.conv2 = nn.Conv1d(in_channels=2, out_channels=4, kernel_size=2, stride=2, padding=2)
        self.conv3 = nn.Conv1d(in_channels=4, out_channels=4, kernel_size=1, stride=1, padding=0)
        self.conv4 = nn.Conv1d(in_channels=4, out_channels=1, kernel_size=1, stride=1, padding=0)

        self._initialize_weights()

    def _initialize_weights(self):
        nn.init.xavier_uniform_(self.fc.weight)
        nn.init.zeros_(self.fc.bias)

        for conv in (self.conv1, self.conv2, self.conv3, self.conv4):
            nn.init.xavier_uniform_(conv.weight)
            nn.init.zeros_(conv.bias)

    def forward(self, msg: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        """Encrypt the message using Alice's network.

        Args:
            msg: torch.Tensor with shape [batch_size, msg_length]
            key: torch.Tensor with shape [batch_size, msg_length]

        Returns:
            torch.Tensor with shape [batch_size, msg_length]
        """
        if msg.shape[1] != self.msg_length or key.shape[1] != self.msg_length:
            raise ValueError(
                f"msg and key must have length {self.msg_length}, "
                f"got {msg.shape[1]} and {key.shape[1]}"
            )

        x = torch.cat([msg, key], dim=1)
        x = torch.sigmoid(self.fc(x))
        x = x.unsqueeze(1)
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = torch.tanh(self.conv4(x))
        x = x.squeeze(1)
        return x


def generate_data(batch_size: int, msg_length: int) -> tuple[torch.Tensor, torch.Tensor]:
    msg = torch.rand(batch_size, msg_length) * 2 - 1
    key = torch.rand(batch_size, msg_length) * 2 - 1
    return msg, key


if __name__ == "__main__":
    N = 16
    batch_size = 64

    alice = AliceNet(msg_length=N)
    msg, key = generate_data(batch_size=batch_size, msg_length=N)
    ciphertext = alice(msg, key)

    print("msg shape:", msg.shape)
    print("key shape:", key.shape)
    print("ciphertext shape:", ciphertext.shape)
    print("ciphertext min/max:", ciphertext.min().item(), ciphertext.max().item())
