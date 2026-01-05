"""
Device selection utility for DeepMana.
Handles safe detection of CUDA, MPS (Apple Silicon), and CPU fallbacks.
"""
import torch
import os
import json
from typing import Optional

CONFIG_FILE = "training_config.json"

def get_compute_device(config_path: str = CONFIG_FILE) -> torch.device:
    """
    Select compute device based on config file and hardware availability.
    
    Priority:
    1. Force Override (from config)
    2. CUDA (if 'auto' and available)
    3. MPS (if 'auto' and available)
    4. CPU (fallback)
    """
    # 1. Load preference from config
    device_pref = "auto"
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                data = json.load(f)
                device_pref = data.get("device", "auto").lower()
        except:
            pass  # Fail silently to defaults

    # 2. Logic Handler
    if device_pref == "cpu":
        return torch.device("cpu")
        
    elif device_pref == "cuda":
        if torch.cuda.is_available():
            return torch.device("cuda")
        print("[WARNING] CUDA requested but not available. Falling back to CPU.")
        return torch.device("cpu")
        
    elif device_pref == "mps":
        if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            return torch.device("mps")
        print("[WARNING] MPS requested but not available. Falling back to CPU.")
        return torch.device("cpu")
        
    else:  # "auto" or unknown
        if torch.cuda.is_available():
            return torch.device("cuda")
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            return torch.device("mps")
        else:
            return torch.device("cpu")

def get_device_name(device: torch.device) -> str:
    """Return human-readable name of the device."""
    if device.type == "cuda":
        return torch.cuda.get_device_name(0)
    elif device.type == "mps":
        return "Apple Silicon GPU (MPS)"
    else:
        return "CPU"
