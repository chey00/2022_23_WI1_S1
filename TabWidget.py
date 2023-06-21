from PyQt6.QtWidgets import QTabWidget

from DatabaseWidget import DatabaseWidget
from DrawWidget import DrawWidget


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        database = DatabaseWidget(parent)
        draw = DrawWidget(parent)

        self.addTab(database, "Datenbank")
        self.addTab(draw, "Zeichnen")
