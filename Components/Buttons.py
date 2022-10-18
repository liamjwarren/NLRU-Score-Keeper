from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel

from SocialMedia.facebook import Facebook
from SocialMedia.twitter import Twitter

TRY = 5
CONVERSION = 2
PENALTY = 3

class OtherButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('<h1>Game Management</h1>')
        self.facebook = Facebook()
        self.twitter = Twitter()
        self.halfTime = QPushButton('Half Time')
        self.halfTime.clicked.connect(self.handleHalfTime)
        self.fullTime = QPushButton('Full Time')
        self.fullTime.clicked.connect(self.handleFullTime)

        self.overallLayout = QVBoxLayout()
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.halfTime)
        self.layout.addWidget(self.fullTime)
        self.overallLayout.addWidget(self.label)
        self.overallLayout.addLayout(self.layout)
        self.setLayout(self.overallLayout)

    def handleHalfTime(self):
        self.facebook.postHalfTimeScore()
        self.twitter.postHalfTimeScore()

    def handleFullTime(self):
        self.clearScore()
        self.facebook.postFullTimeScore()
        self.twitter.postFullTimeScore()
        
    def clearScore(self):
        fhw = open("output/homeTeamScore.txt", "w")
        fhw.write(str(0))
        fhw.close()
        faw = open("output/awayTeamScore.txt", "w")
        faw.write(str(0))
        faw.close()


class HomeButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.addTry = QPushButton('Add Try')
        self.addTry.clicked.connect(self.handleAddTry)
        self.addConversion = QPushButton('Add Conversion')
        self.addConversion.clicked.connect(self.handleAddConversion)
        self.addPenaltyKick = QPushButton('Add Penalty Kick')
        self.addPenaltyKick.clicked.connect(self.handleAddPenalty)

        self.removeTry = QPushButton('Remove Try')
        self.removeTry.clicked.connect(self.handleRemoveTry)
        self.removeConversion = QPushButton('Remove Conversion')
        self.removeConversion.clicked.connect(self.handleRemoveConversion)
        self.removePenaltyKick = QPushButton('Remove Penalty Kick')
        self.removePenaltyKick.clicked.connect(self.handleRemovePenalty)

        self.layout = QVBoxLayout()
        self.addLayout = QHBoxLayout()
        self.addLayout.addWidget(self.addTry)
        self.addLayout.addWidget(self.addConversion)
        self.addLayout.addWidget(self.addPenaltyKick)

        self.removeLayout = QHBoxLayout()
        self.removeLayout.addWidget(self.removeTry)
        self.removeLayout.addWidget(self.removeConversion)
        self.removeLayout.addWidget(self.removePenaltyKick)

        self.layout.addLayout(self.addLayout)
        self.layout.addLayout(self.removeLayout)

        self.setLayout(self.layout)

    def handleAddTry(self):
        fo = open("output/homeTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        newInt = oldInt + TRY
        newString = str(newInt)
        fw = open("output/homeTeamScore.txt", "w")
        fw.write(newString)
        fw.close()

    def handleRemoveTry(self):
        fo = open("output/homeTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        if oldInt >= TRY:
            newInt = oldInt - TRY
            newString = str(newInt)
            fw = open("output/homeTeamScore.txt", "w")
            fw.write(newString)
            fw.close()

    def handleAddConversion(self):
        fo = open("output/homeTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        newInt = oldInt + CONVERSION
        newString = str(newInt)
        fw = open("output/homeTeamScore.txt", "w")
        fw.write(newString)
        fw.close()

    def handleRemoveConversion(self):
        fo = open("output/homeTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        if oldInt >= CONVERSION:
            newInt = oldInt - CONVERSION
            newString = str(newInt)
            fw = open("output/homeTeamScore.txt", "w")
            fw.write(newString)
            fw.close()

    def handleAddPenalty(self):
        fo = open("output/homeTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        newInt = oldInt + PENALTY
        newString = str(newInt)
        fw = open("output/homeTeamScore.txt", "w")
        fw.write(newString)
        fw.close()

    def handleRemovePenalty(self):
        fo = open("output/homeTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        if oldInt >= PENALTY:
            newInt = oldInt - PENALTY
            newString = str(newInt)
            fw = open("output/homeTeamScore.txt", "w")
            fw.write(newString)
            fw.close()

class AwayButtons(QWidget):
    def __init__(self):
        super().__init__()

        self.addTry = QPushButton('Add Try')
        self.addTry.clicked.connect(self.handleAddTry)
        self.addConversion = QPushButton('Add Conversion')
        self.addConversion.clicked.connect(self.handleAddConversion)
        self.addPenaltyKick = QPushButton('Add Penalty Kick')
        self.addPenaltyKick.clicked.connect(self.handleAddPenalty)

        self.removeTry = QPushButton('Remove Try')
        self.removeTry.clicked.connect(self.handleRemoveTry)
        self.removeConversion = QPushButton('Remove Conversion')
        self.removeConversion.clicked.connect(self.handleRemoveConversion)
        self.removePenaltyKick = QPushButton('Remove Penalty Kick')
        self.removePenaltyKick.clicked.connect(self.handleRemovePenalty)

        self.layout = QVBoxLayout()
        self.addLayout = QHBoxLayout()
        self.addLayout.addWidget(self.addTry)
        self.addLayout.addWidget(self.addConversion)
        self.addLayout.addWidget(self.addPenaltyKick)

        self.removeLayout = QHBoxLayout()
        self.removeLayout.addWidget(self.removeTry)
        self.removeLayout.addWidget(self.removeConversion)
        self.removeLayout.addWidget(self.removePenaltyKick)

        self.layout.addLayout(self.addLayout)
        self.layout.addLayout(self.removeLayout)

        self.setLayout(self.layout)

    def handleAddTry(self):
        fo = open("output/awayTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        newInt = oldInt + TRY
        newString = str(newInt)
        fw = open("output/awayTeamScore.txt", "w")
        fw.write(newString)
        fw.close()

    def handleRemoveTry(self):
        fo = open("output/awayTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        if oldInt >= TRY:
            newInt = oldInt - TRY
            newString = str(newInt)
            fw = open("output/awayTeamScore.txt", "w")
            fw.write(newString)
            fw.close()

    def handleAddConversion(self):
        fo = open("output/awayTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        newInt = oldInt + CONVERSION
        newString = str(newInt)
        fw = open("output/awayTeamScore.txt", "w")
        fw.write(newString)
        fw.close()

    def handleRemoveConversion(self):
        fo = open("output/awayTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        if oldInt >= CONVERSION:
            newInt = oldInt - CONVERSION
            newString = str(newInt)
            fw = open("output/awayTeamScore.txt", "w")
            fw.write(newString)
            fw.close()

    def handleAddPenalty(self):
        fo = open("output/awayTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        newInt = oldInt + PENALTY
        newString = str(newInt)
        fw = open("output/awayTeamScore.txt", "w")
        fw.write(newString)
        fw.close()

    def handleRemovePenalty(self):
        fo = open("output/awayTeamScore.txt", "r")
        oldRead = fo.read()
        fo.close()
        oldInt = int(oldRead)
        if oldInt >= PENALTY:
            newInt = oldInt - PENALTY
            newString = str(newInt)
            fw = open("output/awayTeamScore.txt", "w")
            fw.write(newString)
            fw.close()
