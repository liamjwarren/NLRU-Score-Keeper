from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import QFileSystemWatcher, Qt

homeTeamNamePath = "output/homeTeamName.txt"
homeTeamScorePath = "output/homeTeamScore.txt"
awayTeamNamePath = "output/awayTeamName.txt"
awayTeamScorePath = "output/awayTeamScore.txt"

class Score(QWidget):
    def __init__(self):
        super().__init__()
        self.homeTeamName = QLabel()
        self.homeTeamName.setAlignment(Qt.AlignCenter)
        self.homeTeamScore = QLabel()
        self.homeTeamScore.setAlignment(Qt.AlignCenter)
        self.awayTeamName = QLabel()
        self.awayTeamName.setAlignment(Qt.AlignCenter)
        self.awayTeamScore = QLabel()
        self.awayTeamScore.setAlignment(Qt.AlignCenter)
        self.homeTeamNameWatch = QFileSystemWatcher()
        self.homeTeamNameWatch.addPath(homeTeamNamePath)
        self.homeTeamNameWatch.fileChanged.connect(self.handleHomeTeamNameChange)
        self.homeTeamScoreWatch = QFileSystemWatcher()
        self.homeTeamScoreWatch.addPath(homeTeamScorePath)
        self.homeTeamScoreWatch.fileChanged.connect(self.handleHomeTeamScoreChange)
        self.awayTeamNameWatch = QFileSystemWatcher()
        self.awayTeamNameWatch.addPath(awayTeamNamePath)
        self.awayTeamNameWatch.fileChanged.connect(self.handleAwayTeamNameChange)
        self.awayTeamScoreWatch = QFileSystemWatcher()
        self.awayTeamScoreWatch.addPath(awayTeamScorePath)
        self.awayTeamScoreWatch.fileChanged.connect(self.handleAwayTeamScoreChange)

        self.overallLayout = QVBoxLayout()
        self.nameLayout = QHBoxLayout()
        self.scoreLayout = QHBoxLayout()
        self.nameLayout.addWidget(self.homeTeamName)
        self.scoreLayout.addWidget(self.homeTeamScore)
        self.nameLayout.addWidget(self.awayTeamName)
        self.scoreLayout.addWidget(self.awayTeamScore)
        self.overallLayout.addLayout(self.nameLayout)
        self.overallLayout.addLayout(self.scoreLayout)
        self.setLayout(self.overallLayout)

    def handleHomeTeamNameChange(self):
        fo = open("output/homeTeamName.txt", "r")
        read = fo.read()
        self.homeTeamName.setText("<h2>"+ read + "</h2>")
        fo.close()

    def handleHomeTeamScoreChange(self):
        fo = open("output/homeTeamScore.txt", "r")
        read = fo.read()
        self.homeTeamScore.setText("<h1>"+ read + "</h1>")
        fo.close()

    def handleAwayTeamNameChange(self):
        fo = open("output/awayTeamName.txt", "r")
        read = fo.read()
        self.awayTeamName.setText("<h2>"+ read + "</h2>")
        fo.close()

    def handleAwayTeamScoreChange(self):
        fo = open("output/awayTeamScore.txt", "r")
        read = fo.read()
        self.awayTeamScore.setText("<h1>"+ read + "</h1>")
        fo.close()
