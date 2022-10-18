from PyQt5.QtWidgets import QTextEdit, QWidget, QLineEdit, QVBoxLayout, QLabel, QHBoxLayout

from Components.Buttons import AwayButtons

class AwayTeam(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = AwayButtons()
        self.teamInput = QLineEdit()
        self.teamInput.textChanged.connect(self.selectionChanged)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.teamInput)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

    def selectionChanged(self):
        file = open("output/awayTeamName.txt", "w")
        file.write(self.teamInput.text())
        file.close()
