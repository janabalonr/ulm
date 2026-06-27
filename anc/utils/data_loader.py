"""Data loading utilities for Adversarial Neural Cryptography."""

import torch
from data.config import MSG_LEN, BATCH_SIZE


def get_data():
    """
    Generate and load training data.
    
    Returns:
        dict: Dictionary containing training data tensors
    """
    # Generate random plaintext messages
    plaintexts = torch.randint(0, 2, (BATCH_SIZE, MSG_LEN), dtype=torch.float32)
    
    # Generate random keys
    keys = torch.randint(0, 2, (BATCH_SIZE, MSG_LEN), dtype=torch.float32)
    
    return {
        'plaintexts': plaintexts,
        'keys': keys,
    }
