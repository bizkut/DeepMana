"""
DeepMana AI Overlay - Action Queue System.
Shows a step-by-step list of actions to perform during your turn.
"""

import sys
import math
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, 
                              QVBoxLayout, QHBoxLayout, QFrame, QScrollArea)
from PyQt6.QtGui import QFont, QColor, QPainter, QPen, QBrush, QRadialGradient
from PyQt6.QtCore import Qt, QTimer, QPointF, QRectF

class ActionItem(QFrame):
    """Single action item in the queue."""
    def __init__(self, step_num: int, action_type: str, description: str, details: str = ""):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: #2a2a2a;
                border-radius: 6px;
                margin: 2px 0px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)
        
        # Step number
        step_label = QLabel(str(step_num))
        step_label.setFixedSize(24, 24)
        step_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        step_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        
        # Color based on action type
        if "PLAY" in action_type.upper():
            color = "#4ec9b0"  # Green
        elif "ATTACK" in action_type.upper():
            color = "#f14c4c"  # Red
        elif "HERO" in action_type.upper():
            color = "#dcdcaa"  # Yellow
        else:
            color = "#0078d4"  # Blue
            
        step_label.setStyleSheet(f"""
            background-color: {color};
            color: #1a1a1a;
            border-radius: 12px;
            font-weight: bold;
        """)
        layout.addWidget(step_label)
        
        # Text content
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        
        desc_label = QLabel(description)
        desc_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        desc_label.setStyleSheet(f"color: {color}; background: transparent;")
        text_layout.addWidget(desc_label)
        
        if details:
            detail_label = QLabel(details)
            detail_label.setFont(QFont("Segoe UI", 9))
            detail_label.setStyleSheet("color: #8a8a8a; background: transparent;")
            detail_label.setWordWrap(True)
            text_layout.addWidget(detail_label)
        
        layout.addLayout(text_layout)
        layout.addStretch()


class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepMana AI Overlay")
        
        # Animation
        self.anim_tick = 0
        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self._animate)
        self.anim_timer.start(33)
        
        # Game state
        self.arrow_start = None
        self.arrow_end = None
        self.highlight_pos = None
        self.action_queue = []  # List of (type, desc, details)
        
        # Window config
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        
        if QApplication.primaryScreen():
            screen_geo = QApplication.primaryScreen().geometry()
            self.setGeometry(screen_geo)
        else:
            self.setGeometry(0, 0, 1920, 1080)

        # Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(10)
        
        # Main Panel
        self.panel = QFrame()
        self.panel.setFixedWidth(340)
        self.panel.setMaximumHeight(500)
        self.panel.setStyleSheet("""
            QFrame {
                background-color: rgba(26, 26, 26, 245);
                border: 1px solid #2a2a2a;
                border-radius: 8px;
            }
        """)
        panel_layout = QVBoxLayout(self.panel)
        panel_layout.setContentsMargins(16, 14, 16, 14)
        panel_layout.setSpacing(10)

        # Header
        header_row = QHBoxLayout()
        self.title_label = QLabel("DEEPMANA AI")
        self.title_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #8a8a8a; background: transparent; letter-spacing: 0.5px;")
        header_row.addWidget(self.title_label)
        header_row.addStretch()
        
        self.status_text = QLabel("● ANALYZING")
        self.status_text.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.status_text.setStyleSheet("color: #4ec9b0; background: transparent;")
        header_row.addWidget(self.status_text)
        panel_layout.addLayout(header_row)
        
        # Separator
        sep = QFrame()
        sep.setFixedHeight(1)
        sep.setStyleSheet("background: #2a2a2a;")
        panel_layout.addWidget(sep)
        
        # Action Queue Title
        queue_header = QHBoxLayout()
        queue_title = QLabel("ACTIONS À EFFECTUER")
        queue_title.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        queue_title.setStyleSheet("color: #8a8a8a; background: transparent; letter-spacing: 0.5px;")
        queue_header.addWidget(queue_title)
        queue_header.addStretch()
        
        self.action_count = QLabel("0 actions")
        self.action_count.setFont(QFont("Segoe UI", 9))
        self.action_count.setStyleSheet("color: #0078d4; background: transparent;")
        queue_header.addWidget(self.action_count)
        panel_layout.addLayout(queue_header)
        
        # Action List Container
        self.action_container = QVBoxLayout()
        self.action_container.setSpacing(4)
        panel_layout.addLayout(self.action_container)
        
        # Info text at bottom
        sep2 = QFrame()
        sep2.setFixedHeight(1)
        sep2.setStyleSheet("background: #2a2a2a;")
        panel_layout.addWidget(sep2)
        
        # Stats row
        stats_row = QHBoxLayout()
        
        # Mana
        mana_col = QVBoxLayout()
        mana_label = QLabel("MANA")
        mana_label.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        mana_label.setStyleSheet("color: #8a8a8a; background: transparent;")
        mana_col.addWidget(mana_label)
        self.mana_value = QLabel("0/0")
        self.mana_value.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.mana_value.setStyleSheet("color: #0078d4; background: transparent;")
        mana_col.addWidget(self.mana_value)
        stats_row.addLayout(mana_col)
        
        stats_row.addStretch()
        
        # Win Rate
        wr_col = QVBoxLayout()
        wr_label = QLabel("WIN %")
        wr_label.setFont(QFont("Segoe UI", 8, QFont.Weight.Bold))
        wr_label.setStyleSheet("color: #8a8a8a; background: transparent;")
        wr_col.addWidget(wr_label, alignment=Qt.AlignmentFlag.AlignRight)
        self.winrate_value = QLabel("50%")
        self.winrate_value.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.winrate_value.setStyleSheet("color: #0078d4; background: transparent;")
        wr_col.addWidget(self.winrate_value, alignment=Qt.AlignmentFlag.AlignRight)
        stats_row.addLayout(wr_col)
        
        panel_layout.addLayout(stats_row)
        self.win_prob = 0.5
        
        self.main_layout.addWidget(self.panel)

    def _animate(self):
        self.anim_tick = (self.anim_tick + 1) % 360
        self.update()

    def set_action_queue(self, actions: list):
        """
        Set the action queue.
        actions: list of (action_type, description, details)
        """
        # Clear existing
        while self.action_container.count():
            item = self.action_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        self.action_queue = actions
        self.action_count.setText(f"{len(actions)} action{'s' if len(actions) != 1 else ''}")
        
        for i, (action_type, desc, details) in enumerate(actions):
            item = ActionItem(i + 1, action_type, desc, details)
            self.action_container.addWidget(item)
        
        if not actions:
            no_action = QLabel("Aucune action disponible")
            no_action.setFont(QFont("Segoe UI", 10))
            no_action.setStyleSheet("color: #8a8a8a; background: transparent; padding: 10px;")
            self.action_container.addWidget(no_action)

    def update_status(self, text):
        """Update status (called by old API for compatibility)."""
        # Parse single action into queue
        if text:
            if "END TURN" in text.upper():
                self.set_action_queue([("END", "Fin du tour", "Aucune autre action profitable")])
            else:
                self.set_action_queue([(text.split(":")[0] if ":" in text else "ACTION", text, "")])
        
    def update_info(self, text):
        """Compatibility - add as detail to last action."""
        pass
        
    def update_winrate(self, value):
        self.win_prob = (value + 1) / 2
        pct = int(self.win_prob * 100)
        self.winrate_value.setText(f"{pct}%")
        
        if pct > 60:
            self.winrate_value.setStyleSheet("color: #4ec9b0; background: transparent;")
        elif pct < 40:
            self.winrate_value.setStyleSheet("color: #f14c4c; background: transparent;")
        else:
            self.winrate_value.setStyleSheet("color: #0078d4; background: transparent;")
            
    def update_mana(self, current, maximum):
        self.mana_value.setText(f"{current}/{maximum}")
        
    def set_arrow(self, start, end):
        self.arrow_start = start
        self.arrow_end = end
        self.highlight_pos = None
        self.update()
    
    def set_highlight(self, pos):
        self.highlight_pos = pos
        self.arrow_start = None
        self.arrow_end = None
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        pulse = (math.sin(self.anim_tick * 0.1) + 1) / 2
        
        if self.arrow_start and self.arrow_end:
            start_pt = QPointF(float(self.arrow_start.x), float(self.arrow_start.y))
            end_pt = QPointF(float(self.arrow_end.x), float(self.arrow_end.y))
            
            # Glow
            glow_pen = QPen(QColor(241, 76, 76, 60 + int(40 * pulse)), 14)
            glow_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(glow_pen)
            painter.drawLine(start_pt, end_pt)
            
            # Line
            line_pen = QPen(QColor(241, 76, 76, 255), 3)
            line_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(line_pen)
            painter.drawLine(start_pt, end_pt)
            
            # Target
            radius = 25 + (6 * pulse)
            grad = QRadialGradient(end_pt, radius)
            grad.setColorAt(0, QColor(241, 76, 76, 150))
            grad.setColorAt(1, QColor(241, 76, 76, 0))
            painter.setBrush(QBrush(grad))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(end_pt, radius, radius)
            
            painter.setBrush(QColor(255, 255, 255, 200))
            painter.drawEllipse(end_pt, 4, 4)
        
        elif self.highlight_pos:
            pos = QPointF(float(self.highlight_pos.x), float(self.highlight_pos.y))
            radius = 35 + (8 * pulse)
            
            ring_pen = QPen(QColor(78, 201, 176, 200), 3)
            painter.setPen(ring_pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(pos, radius, radius)
            
            fill_grad = QRadialGradient(pos, radius)
            fill_grad.setColorAt(0, QColor(78, 201, 176, 60))
            fill_grad.setColorAt(1, QColor(78, 201, 176, 0))
            painter.setBrush(QBrush(fill_grad))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(pos, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayWindow()
    
    # Demo action queue
    window.set_action_queue([
        ("PLAY", "Jouer Murloc (2 mana)", "Main position 3 → Board"),
        ("PLAY", "Jouer Sort de Feu (3 mana)", "Main position 1 → Cibler héros adverse"),
        ("ATTACK", "Attaquer avec Golem → Face", "Serviteur 1 → Héros adverse"),
        ("END", "Fin du tour", ""),
    ])
    window.update_mana(6, 10)
    
    window.show()
    print("Overlay demo started.")
    sys.exit(app.exec())
