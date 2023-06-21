from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtWidgets import QWidget


class DrawWidget(QWidget):
    def __init__(self, parent):
        super(DrawWidget, self).__init__(parent)

        self.update()

    def paintEvent(self, a0) -> None:
        super(DrawWidget, self).paintEvent(a0)

        painter = QPainter(self)

        # Aufgabe 3
