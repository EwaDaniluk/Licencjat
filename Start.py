from PyQt5 import QtCore, QtGui, QtWidgets
from Main import Ui_Main

class Ui_Start(object):
    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()
        Start.close()


    def setupUi(self, Start):
        Start.setObjectName("Start")
        Start.resize(1000, 700)
        Start.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.start_pushButton = QtWidgets.QPushButton(Start, clicked=lambda: self.openWindow())
        self.start_pushButton.setGeometry(QtCore.QRect(450, 450, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setStyleSheet("")
        self.start_pushButton.setObjectName("start_pushButton")
        self.label_1 = QtWidgets.QLabel(Start)
        self.label_1.setGeometry(QtCore.QRect(150, 210, 780, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Start)
        self.label_2.setGeometry(QtCore.QRect(370, 280, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Start)
        self.label_3.setGeometry(QtCore.QRect(390, 340, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

    def retranslateUi(self, Start):
        _translate = QtCore.QCoreApplication.translate
        Start.setWindowTitle(_translate("Start", "Start"))
        self.start_pushButton.setText(_translate("Start", "Start"))
        self.label_1.setText(_translate("Start", "Program pozwala trenować agenta w prostych grach 2D przy pomocy 3 algorytmów."))
        self.label_2.setText(_translate("Start", "Gry: Cart Pole, Car Racing, Taxi"))
        self.label_3.setText(_translate("Start", "Algorytmy: DQN, A2C, PPO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Start = QtWidgets.QWidget()
    ui = Ui_Start()
    ui.setupUi(Start)
    Start.show()
    sys.exit(app.exec_())
