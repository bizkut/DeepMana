from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame, 
                             QLabel, QSpinBox, QComboBox, QPushButton, QFormLayout, QCheckBox)
from PyQt6.QtCore import Qt
import json
import os

CONFIG_FILE = "training_config.json"

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(20)
        
        # Title
        title = QLabel("System Configuration")
        title.setStyleSheet("font-size: 28px; font-weight: 600; color: #ffffff; margin-bottom: 20px;")
        self.layout.addWidget(title)
        
        # Config Card
        card = QFrame()
        card.setObjectName("dash_card")
        form_layout = QFormLayout(card)
        form_layout.setContentsMargins(30, 30, 30, 30)
        form_layout.setSpacing(25)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # 1. Hardware Settings
        self.spin_workers = QSpinBox()
        self.spin_workers.setRange(0, 32)
        self.spin_workers.setValue(8)
        self.spin_workers.setSuffix(" cores")
        
        self.combo_device = QComboBox()
        self.combo_device.addItems([
            "Auto (CUDA > MPS > CPU)",  # Auto-detect best available
            "Force CPU",
            "Force CUDA",
            "Force MPS"  # Apple Silicon GPU
        ])
        
        form_layout.addRow(self.create_label("CPU WORKERS", "Parallel processes for self-play collection"), self.spin_workers)
        form_layout.addRow(self.create_label("COMPUTE DEVICE", "Hardware accelerator used for neural updates"), self.combo_device)
        
        # 2. Training Hyperparameters
        self.spin_batch = QSpinBox()
        self.spin_batch.setRange(16, 512)
        self.spin_batch.setValue(64)
        self.spin_batch.setSingleStep(16)
        
        self.spin_mcts = QSpinBox()
        self.spin_mcts.setRange(10, 800)
        self.spin_mcts.setValue(25)
        
        self.spin_games = QSpinBox()
        self.spin_games.setRange(20, 200)
        self.spin_games.setValue(40)
        self.spin_games.setSingleStep(10)
        
        form_layout.addRow(self.create_label("BATCH SIZE", "Number of training samples per neural update"), self.spin_batch)
        form_layout.addRow(self.create_label("MCTS SIMULATIONS", "Thinking steps per decision during games"), self.spin_mcts)
        form_layout.addRow(self.create_label("GAMES PER ITERATION", "Self-play games per training cycle"), self.spin_games)
        
        
        self.layout.addWidget(card)
        
        self.layout.addSpacing(20)
        
        # Save Button
        self.btn_save = QPushButton("SAVE CONFIGURATION")
        self.btn_save.setObjectName("neural-btn")
        self.btn_save.setFixedHeight(44)
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_save.clicked.connect(self.save_config)
        self.layout.addWidget(self.btn_save)
        
        self.layout.addStretch()
        
        self.load_config()
 
    def create_label(self, text, subtext):
        wid = QWidget()
        lay = QVBoxLayout(wid)
        lay.setContentsMargins(0,0,0,0)
        lay.setSpacing(4)
        l1 = QLabel(text)
        l1.setStyleSheet("font-size: 11px; color: #8a8a8a; font-weight: 600; letter-spacing: 0.5px;")
        l2 = QLabel(subtext)
        l2.setStyleSheet("font-size: 13px; color: #4a4a4a; font-weight: 400;")
        lay.addWidget(l1)
        lay.addWidget(l2)
        return wid

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    self.spin_workers.setValue(data.get("workers", 8))
                    self.spin_batch.setValue(data.get("batch_size", 64))
                    self.spin_mcts.setValue(data.get("mcts_sims", 25))
                    self.spin_games.setValue(data.get("games_per_iter", 40))
                    # Device: map stored name to combo index
                    device_map = {"auto": 0, "cpu": 1, "cuda": 2, "mps": 3}
                    device = data.get("device", "auto")
                    self.combo_device.setCurrentIndex(device_map.get(device, 0))
            except:
                pass

    def save_config(self):
        # Load existing config to preserve fields not in GUI
        existing = {}
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    existing = json.load(f)
            except:
                pass
        
        # Update with GUI values
        device_options = ["auto", "cpu", "cuda", "mps"]
        existing.update({
            "workers": self.spin_workers.value(),
            "batch_size": self.spin_batch.value(),
            "mcts_sims": self.spin_mcts.value(),
            "games_per_iter": self.spin_games.value(),
            "device": device_options[self.combo_device.currentIndex()]
        })
        
        with open(CONFIG_FILE, 'w') as f:
            json.dump(existing, f, indent=4)
        print("Configuration saved!")
