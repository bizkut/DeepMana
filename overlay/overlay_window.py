"""
DeepMana AI Overlay - Premium Hearthstone Assistant Display.
A transparent, always-on-top window that shows AI suggestions during gameplay.
"""

import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QGraphicsDropShadowEffect
from PyQt6.QtGui import QFont, QColor, QPainter, QPen, QBrush, QLinearGradient, QRadialGradient, QFontDatabase
from PyQt6.QtCore import Qt, QTimer, QPointF, QRectF

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepMana AI Overlay")
        
        # === ANIMATION STATE ===
        self.anim_tick = 0
        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self._animate)
        self.anim_timer.start(33)  # ~30 FPS
        
        # === GAME STATE ===
        self.arrow_start = None
        self.arrow_end = None
        self.highlight_pos = None
        self.action_history = []  # Last 3 suggestions
        
        # === WINDOW CONFIG ===
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        
        # Full screen coverage
        if QApplication.primaryScreen():
            screen_geo = QApplication.primaryScreen().geometry()
            self.setGeometry(screen_geo)
        else:
            self.setGeometry(0, 0, 1920, 1080)

        # === UI LAYOUT ===
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)
        
        # === MAIN PANEL (Glassmorphism) ===
        self.panel = QFrame()
        self.panel.setFixedWidth(380)
        self.panel.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(15, 23, 42, 220),
                    stop:1 rgba(30, 41, 59, 200));
                border: 1px solid rgba(56, 189, 248, 60);
                border-radius: 16px;
            }
        """)
        panel_layout = QVBoxLayout(self.panel)
        panel_layout.setContentsMargins(20, 16, 20, 16)
        panel_layout.setSpacing(8)

        # Header Row
        header_row = QHBoxLayout()
        
        # AI Status Title
        self.title_label = QLabel("⚡ DEEPMANA AI")
        self.title_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #38bdf8; background: transparent; border: none; letter-spacing: 1px;")
        header_row.addWidget(self.title_label)
        header_row.addStretch()
        
        # Status Indicator
        self.status_dot = QLabel("●")
        self.status_dot.setStyleSheet("color: #4ade80; font-size: 12px; background: transparent; border: none;")
        header_row.addWidget(self.status_dot)
        
        self.status_text = QLabel("ACTIVE")
        self.status_text.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.status_text.setStyleSheet("color: #4ade80; background: transparent; border: none;")
        header_row.addWidget(self.status_text)
        
        panel_layout.addLayout(header_row)
        
        # Separator
        sep = QFrame()
        sep.setFixedHeight(1)
        sep.setStyleSheet("background: rgba(148, 163, 184, 30); border: none;")
        panel_layout.addWidget(sep)
        
        # Main Suggestion Label
        self.suggestion_label = QLabel("ANALYZING...")
        self.suggestion_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Black))
        self.suggestion_label.setStyleSheet("color: #ffffff; background: transparent; border: none;")
        self.suggestion_label.setWordWrap(True)
        panel_layout.addWidget(self.suggestion_label)
        
        # Detail Label
        self.info_label = QLabel("Waiting for game state...")
        self.info_label.setFont(QFont("Segoe UI", 11))
        self.info_label.setStyleSheet("color: #94a3b8; background: transparent; border: none;")
        self.info_label.setWordWrap(True)
        panel_layout.addWidget(self.info_label)
        
        # Winrate Section
        winrate_container = QWidget()
        winrate_container.setStyleSheet("background: transparent; border: none;")
        winrate_layout = QVBoxLayout(winrate_container)
        winrate_layout.setContentsMargins(0, 8, 0, 0)
        winrate_layout.setSpacing(6)
        
        # Winrate Header
        wr_header = QHBoxLayout()
        self.winrate_label = QLabel("WIN PROBABILITY")
        self.winrate_label.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.winrate_label.setStyleSheet("color: #64748b; background: transparent; border: none; letter-spacing: 0.5px;")
        wr_header.addWidget(self.winrate_label)
        wr_header.addStretch()
        
        self.winrate_value = QLabel("50%")
        self.winrate_value.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.winrate_value.setStyleSheet("color: #38bdf8; background: transparent; border: none;")
        wr_header.addWidget(self.winrate_value)
        
        winrate_layout.addLayout(wr_header)
        
        # Progress Bar Container (drawn in paintEvent)
        self.win_prob = 0.5
        self.winrate_bar = QWidget()
        self.winrate_bar.setFixedHeight(8)
        self.winrate_bar.setStyleSheet("background: transparent; border: none;")
        winrate_layout.addWidget(self.winrate_bar)
        
        panel_layout.addWidget(winrate_container)
        
        # Separator
        sep2 = QFrame()
        sep2.setFixedHeight(1)
        sep2.setStyleSheet("background: rgba(148, 163, 184, 30); border: none;")
        panel_layout.addWidget(sep2)
        
        # Action History
        history_label = QLabel("RECENT SUGGESTIONS")
        history_label.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        history_label.setStyleSheet("color: #64748b; background: transparent; border: none; letter-spacing: 0.5px;")
        panel_layout.addWidget(history_label)
        
        self.history_container = QVBoxLayout()
        self.history_container.setSpacing(4)
        for _ in range(3):
            h_label = QLabel("—")
            h_label.setFont(QFont("Segoe UI", 10))
            h_label.setStyleSheet("color: #475569; background: transparent; border: none;")
            self.history_container.addWidget(h_label)
        panel_layout.addLayout(self.history_container)
        
        # Mana Display
        mana_row = QHBoxLayout()
        self.mana_label = QLabel("⬡ MANA")
        self.mana_label.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.mana_label.setStyleSheet("color: #64748b; background: transparent; border: none;")
        mana_row.addWidget(self.mana_label)
        mana_row.addStretch()
        
        self.mana_value = QLabel("0/0")
        self.mana_value.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.mana_value.setStyleSheet("color: #3b82f6; background: transparent; border: none;")
        mana_row.addWidget(self.mana_value)
        panel_layout.addLayout(mana_row)
        
        self.main_layout.addWidget(self.panel)

    def _animate(self):
        """Update animation tick and repaint."""
        self.anim_tick = (self.anim_tick + 1) % 360
        self.update()

    def update_winrate(self, value):
        """Update winrate percentage (expects value -1 to 1)."""
        self.win_prob = (value + 1) / 2
        pct = int(self.win_prob * 100)
        self.winrate_value.setText(f"{pct}%")
        
        if pct > 60:
            self.winrate_value.setStyleSheet("color: #4ade80; background: transparent; border: none;")
        elif pct < 40:
            self.winrate_value.setStyleSheet("color: #f87171; background: transparent; border: none;")
        else:
            self.winrate_value.setStyleSheet("color: #38bdf8; background: transparent; border: none;")
            
    def update_status(self, text):
        """Update the main suggestion text."""
        self.suggestion_label.setText(text.upper())
        
        # Add to history
        self.action_history.insert(0, text)
        if len(self.action_history) > 3:
            self.action_history.pop()
        
        # Update history labels
        for i, label in enumerate(self._get_history_labels()):
            if i < len(self.action_history):
                label.setText(f"→ {self.action_history[i]}")
                label.setStyleSheet("color: #64748b; background: transparent; border: none;")
            else:
                label.setText("—")
                label.setStyleSheet("color: #475569; background: transparent; border: none;")
        
        # Color based on action type
        if "PLAY" in text.upper():
            self.suggestion_label.setStyleSheet("color: #4ade80; background: transparent; border: none;")
        elif "ATTACK" in text.upper():
            self.suggestion_label.setStyleSheet("color: #f87171; background: transparent; border: none;")
        elif "END TURN" in text.upper():
            self.suggestion_label.setStyleSheet("color: #fbbf24; background: transparent; border: none;")
        else:
            self.suggestion_label.setStyleSheet("color: #38bdf8; background: transparent; border: none;")

    def _get_history_labels(self):
        """Get the 3 history labels from the layout."""
        labels = []
        for i in range(self.history_container.count()):
            item = self.history_container.itemAt(i)
            if item and item.widget():
                labels.append(item.widget())
        return labels

    def update_info(self, text):
        self.info_label.setText(text)
        
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
        
        # --- DRAW WINRATE BAR ---
        bar_width = 340
        bar_height = 8
        bar_x = 40
        bar_y = 228
        
        # Background
        painter.setBrush(QColor(30, 41, 59, 255))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(QRectF(bar_x, bar_y, bar_width, bar_height), 4, 4)
        
        # Gradient fill based on winrate
        fill_width = bar_width * self.win_prob
        if self.win_prob > 0.6:
            grad = QLinearGradient(bar_x, 0, bar_x + fill_width, 0)
            grad.setColorAt(0, QColor(74, 222, 128))
            grad.setColorAt(1, QColor(34, 197, 94))
        elif self.win_prob < 0.4:
            grad = QLinearGradient(bar_x, 0, bar_x + fill_width, 0)
            grad.setColorAt(0, QColor(248, 113, 113))
            grad.setColorAt(1, QColor(239, 68, 68))
        else:
            grad = QLinearGradient(bar_x, 0, bar_x + fill_width, 0)
            grad.setColorAt(0, QColor(56, 189, 248))
            grad.setColorAt(1, QColor(14, 165, 233))
        
        painter.setBrush(QBrush(grad))
        painter.drawRoundedRect(QRectF(bar_x, bar_y, fill_width, bar_height), 4, 4)

        # --- DRAW GAME ELEMENTS ---
        pulse = (math.sin(self.anim_tick * 0.1) + 1) / 2
        
        if self.arrow_start and self.arrow_end:
            start_pt = QPointF(float(self.arrow_start.x), float(self.arrow_start.y))
            end_pt = QPointF(float(self.arrow_end.x), float(self.arrow_end.y))
            
            # Outer glow
            glow_pen = QPen(QColor(248, 113, 113, 60 + int(40 * pulse)), 16)
            glow_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(glow_pen)
            painter.drawLine(start_pt, end_pt)
            
            # Main line
            line_pen = QPen(QColor(248, 113, 113, 255), 4)
            line_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(line_pen)
            painter.drawLine(start_pt, end_pt)
            
            # Target circle
            radius = 30 + (8 * pulse)
            grad = QRadialGradient(end_pt, radius)
            grad.setColorAt(0, QColor(248, 113, 113, 180))
            grad.setColorAt(1, QColor(248, 113, 113, 0))
            painter.setBrush(QBrush(grad))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(end_pt, radius, radius)
            
            # Core dot
            painter.setBrush(QColor(255, 255, 255, 220))
            painter.drawEllipse(end_pt, 5, 5)
        
        elif self.highlight_pos:
            pos = QPointF(float(self.highlight_pos.x), float(self.highlight_pos.y))
            
            # Radiating ring
            radius = 45 + (12 * pulse)
            
            ring_pen = QPen(QColor(74, 222, 128, 220), 4)
            painter.setPen(ring_pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(pos, radius, radius)
            
            # Inner glow
            fill_grad = QRadialGradient(pos, radius)
            fill_grad.setColorAt(0, QColor(74, 222, 128, 80))
            fill_grad.setColorAt(1, QColor(74, 222, 128, 0))
            painter.setBrush(QBrush(fill_grad))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(pos, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayWindow()
    window.show()
    print("Overlay started.")
    sys.exit(app.exec())
