from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QPushButton


class DatabaseWidget(QWidget):
    def __init__(self, parent):
        super(DatabaseWidget, self).__init__(parent)

        self.prename = QLineEdit()
        self.last_name = QLineEdit()
        self.street_name = QLineEdit()
        self.street_number = QLineEdit()
        self.zipcode = QLineEdit()
        self.place = QLineEdit()
        self.phone_number = QLineEdit()

        self.save_button = QPushButton("Speichern")

        layout = QGridLayout(parent)

        # Aufgabe 2.1

        self.setLayout(layout)

        # Aufgabe 2.2

        # Aufgabe 2.3

    @pyqtSlot()
    def save_inputs(self):
        # Aufgabe 2.3
        is_valid = None
