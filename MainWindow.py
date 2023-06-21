from PyQt6.QtWidgets import QMainWindow
from TabWidget import TabWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        tab_widget = TabWidget(parent)

        self.setCentralWidget(tab_widget)

        # Aufgabe 1
