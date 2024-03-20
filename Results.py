from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(649, 466)
        Results.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.Info_label = QtWidgets.QLabel(Results)
        self.Info_label.setGeometry(QtCore.QRect(30, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Info_label.setFont(font)
        self.Info_label.setObjectName("Info_label")
        self.mean_label = QtWidgets.QLabel(Results)
        self.mean_label.setGeometry(QtCore.QRect(60, 50, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mean_label.setFont(font)
        self.mean_label.setObjectName("mean_label")
        self.label = QtWidgets.QLabel(Results)
        self.label.setGeometry(QtCore.QRect(40, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Results)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Results)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Results)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Results)
        self.label_5.setGeometry(QtCore.QRect(40, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Results)
        self.label_6.setGeometry(QtCore.QRect(60, 310, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Results)
        self.label_7.setGeometry(QtCore.QRect(40, 360, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.game_label = QtWidgets.QLabel(Results)
        self.game_label.setGeometry(QtCore.QRect(450, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.game_label.setFont(font)
        self.game_label.setObjectName("game_label")
        self.algorythm_label = QtWidgets.QLabel(Results)
        self.algorythm_label.setGeometry(QtCore.QRect(450, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.algorythm_label.setFont(font)
        self.algorythm_label.setObjectName("algorythm_label")
        self.alpha_label = QtWidgets.QLabel(Results)
        self.alpha_label.setGeometry(QtCore.QRect(450, 190, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.alpha_label.setFont(font)
        self.alpha_label.setObjectName("alpha_label")
        self.gamma_label = QtWidgets.QLabel(Results)
        self.gamma_label.setGeometry(QtCore.QRect(450, 225, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gamma_label.setFont(font)
        self.gamma_label.setObjectName("gamma_label")
        self.numbersIteration_label = QtWidgets.QLabel(Results)
        self.numbersIteration_label.setGeometry(QtCore.QRect(450, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numbersIteration_label.setFont(font)
        self.numbersIteration_label.setObjectName("numbersIteration_label")
        self.reward_label = QtWidgets.QLabel(Results)
        self.reward_label.setGeometry(QtCore.QRect(450, 365, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reward_label.setFont(font)
        self.reward_label.setObjectName("reward_label")

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Form"))
        self.Info_label.setText(_translate("Results", "Wyniki uczenia agenta"))
        self.mean_label.setText(_translate("Results", "Prametry:"))
        self.label.setText(_translate("Results", "Gra:"))
        self.label_2.setText(_translate("Results", "Algorytm:"))
        self.label_3.setText(_translate("Results", "Współczynnik uczenia alpha:"))
        self.label_4.setText(_translate("Results", "Współczynnnik dyskontowania gamma:"))
        self.label_5.setText(_translate("Results", "Liczba prób:"))
        self.label_6.setText(_translate("Results", "Wyniki:"))
        self.label_7.setText(_translate("Results", "Średnia nagroda z ostatnich 3 kroków treningu:"))
        self.game_label.setText(_translate("Results", "TextLabel"))
        self.algorythm_label.setText(_translate("Results", "TextLabel"))
        self.alpha_label.setText(_translate("Results", "TextLabel"))
        self.gamma_label.setText(_translate("Results", "TextLabel"))
        self.numbersIteration_label.setText(_translate("Results", "TextLabel"))
        self.reward_label.setText(_translate("Results", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QWidget()
    ui = Ui_Results()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())
