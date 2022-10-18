import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon

from Components.Buttons import OtherButtons
from Components.Score import Score
from Components.HomeTeam import HomeTeam
from Components.AwayTeam import AwayTeam


class Application(QWidget):

    def __init__(self):
        super().__init__()

        self.homeTeam = HomeTeam()
        self.awayTeam = AwayTeam()
        self.gameManagementButtons = OtherButtons()
        self.score = Score()
        self.initOutput()
        self.initApp()

    def initOutput(self):
        fHN = open("output/homeTeamName.txt", "w")
        fHN.write("Please enter home team name")
        fHN.close()

        fHS = open("output/homeTeamScore.txt", "w")
        fHS.write("0")
        fHS.close()

        fAN = open("output/awayTeamName.txt", "w")
        fAN.write("Please enter away team name")
        fAN.close()

        fAS = open("output/awayTeamScore.txt", "w")
        fAS.write("0")
        fAS.close()

    def initApp(self):
        self.setBaseSize(600, 600)
        self.setMinimumSize(600, 600)
        self.setWindowTitle('NLRU Score Keeper')
        self.setWindowIcon(QIcon("nlru.png"))

        self.layout = QVBoxLayout()
        self.teamsLayout = QHBoxLayout()

        self.teamsLayout.addWidget(self.homeTeam)
        self.teamsLayout.addWidget(self.awayTeam)
        self.layout.addWidget(self.score)
        self.layout.addLayout(self.teamsLayout)
        self.layout.addWidget(self.gameManagementButtons)
        self.setLayout(self.layout)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    