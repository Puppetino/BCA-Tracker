from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        # CUSTOM PROPERTIES
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0xFF0000
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.prefix = ""
        self.text_color = 0xFFFFFF
        
        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)
        
    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)
        
    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()
        
    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, event):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value  = self.value * 360 / self.max_value
        
        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))
        
        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)
        
        # PEN FOR CIRCULAR PROGRESS
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)
        paint.setPen(pen)
        
        # DRAW CIRCULAR PROGRESS
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)
        
        # PEN FOR TEXT
        text_pen = QPen()
        text_pen.setColor(QColor(self.text_color))
        paint.setPen(text_pen)
        
        # CREATE TEXT
        paint.drawText(rect, Qt.AlignCenter, f"{self.prefix}{self.value}{self.suffix}")
        
        paint.end()