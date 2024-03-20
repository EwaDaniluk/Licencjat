from PyQt5 import QtCore, QtGui, QtWidgets
from Train_agent import AgentWrapper
from Results import Ui_Results


class Ui_Main(object):
    def avgReward(self):
        with open("wyniki.csv", 'r') as f:
            lines = f.readlines()
        lines = lines[:-1]  # Usuń ostatni wiersz - nazwy kolumn
        lines = lines[1:]    # Usuń pierwszy wiersz
        with open("może_to_sie_uda.txt", "w") as g:
            for line in lines:
                g.write(f"{line}")
        last_lines = lines[-100:]  # Weź 100 ostatnich wierszy
        sum = 0
        for lines in last_lines:
            _, reward = lines.split()  # Rozdziel indeks i liczbę
            sum += float(reward)
        average_reward = round(sum / len(last_lines), 2)
        return average_reward

    def writeParameters(self):
        self.ui.game_label.setText(self.gra_comboBox.currentText())
        self.ui.algorythm_label.setText(self.agent_comboBox.currentText())
        self.ui.alpha_label.setText(self.wspolczynnikUczenia_lineEdit.text())
        self.ui.gamma_label.setText(self.wspolczynnikDyskontowania_lineEdit.text())
        self.ui.numbersIteration_label.setText(self.liczbaProb_lineEdit.text())
        self.ui.reward_label.setText(str(self.avgReward()))

    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Results()
        self.ui.setupUi(self.window)
        self.window.show()
        self.writeParameters()

    def trainAgent(self, training_iteration, lr, gamma, epsilon, env, algorithm):
        if not (0 <= epsilon <= 1):
            self.ifDone_label.setText("Nieprawidłowa wartość epsilon. Powinna być z przedziału <0, 1>.")
            return
        if not (0 < gamma < 1):
            self.ifDone_label.setText("Nieprawidłowa wartość gamma. Powinna być z przedziału (0, 1).")
            return
        if not (0 < lr < 1):
            self.ifDone_label.setText("Nieprawidłowa wartość współczynnika uczenia. Powinna być z przedziału (0, 1).")
            return
        if training_iteration <= 0:
            self.ifDone_label.setText("Nieprawidłowa wartość liczby iteracji. Powinna być większa od zera.")
            return
        wrapper = AgentWrapper(training_iteration, lr, gamma, epsilon, env, algorithm)
        self.ifDone_label.setText("Trening rozpoczęty")
        wrapper.train_agent()
        self.ifDone_label.setText("Trening skończony")

    def chooseEnvironment(self, env):
        if env == "Cart Pole":
            return "CartPole-v1"
        elif env == "Car Racing":
            return "CarRacing-v2"
        else:
            return "Taxi-v3"

    # def chooseAlgorithm(self, algorithm):
    #     if algorithm == "DQN":
    #         return "DQN"
    #     elif algorithm == "A2C":
    #         return "A2C"
    #     else:
    #         return "PPO"

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(2)
        Main.setFont(font)
        Main.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.uruchom_pushButton = QtWidgets.QPushButton(Main,
                                                        clicked=lambda: self.trainAgent(int(self.liczbaProb_lineEdit.text()),
                                                                                        float(self.wspolczynnikUczenia_lineEdit.text()),
                                                                                        float(self.wspolczynnikDyskontowania_lineEdit.text()),
                                                                                        float(self.epsilon_lineEdit.text()),
                                                                                        self.chooseEnvironment((self.gra_comboBox.currentText())),
                                                                                        # self.chooseAlgorithm((self.agent_comboBox.currentText())))
                                                                                        self.agent_comboBox.currentText()))
        self.uruchom_pushButton.setGeometry(QtCore.QRect(450, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.uruchom_pushButton.setFont(font)
        self.uruchom_pushButton.setObjectName("uruchom_pushButton")
        self.gra_comboBox = QtWidgets.QComboBox(Main)
        self.gra_comboBox.setGeometry(QtCore.QRect(530, 120, 92, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gra_comboBox.setFont(font)
        self.gra_comboBox.setObjectName("gra_comboBox")
        self.gra_comboBox.addItem("")
        self.gra_comboBox.addItem("")
        self.gra_comboBox.addItem("")
        self.agent_comboBox = QtWidgets.QComboBox(Main)
        self.agent_comboBox.setGeometry(QtCore.QRect(530, 170, 92, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.agent_comboBox.setFont(font)
        self.agent_comboBox.setObjectName("agent_comboBox")
        self.agent_comboBox.addItem("")
        self.agent_comboBox.addItem("")
        self.agent_comboBox.addItem("")
        self.wspolczynnikUczenia_lineEdit = QtWidgets.QLineEdit(Main)
        self.wspolczynnikUczenia_lineEdit.setGeometry(QtCore.QRect(530, 220, 92, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wspolczynnikUczenia_lineEdit.setFont(font)
        self.wspolczynnikUczenia_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wspolczynnikUczenia_lineEdit.setObjectName("wspolczynnikUczenia_lineEdit")
        self.wspolczynnikDyskontowania_lineEdit = QtWidgets.QLineEdit(Main)
        self.wspolczynnikDyskontowania_lineEdit.setGeometry(QtCore.QRect(530, 270, 92, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wspolczynnikDyskontowania_lineEdit.setFont(font)
        self.wspolczynnikDyskontowania_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.wspolczynnikDyskontowania_lineEdit.setObjectName("wspolczynnikDyskontowania_lineEdit")
        self.epsilon_lineEdit = QtWidgets.QLineEdit(Main)
        self.epsilon_lineEdit.setGeometry(QtCore.QRect(530, 320, 92, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.epsilon_lineEdit.setFont(font)
        self.epsilon_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.epsilon_lineEdit.setObjectName("epsilon_lineEdit")
        self.liczbaProb_lineEdit = QtWidgets.QLineEdit(Main)
        self.liczbaProb_lineEdit.setGeometry(QtCore.QRect(530, 370, 92, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.liczbaProb_lineEdit.setFont(font)
        self.liczbaProb_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.liczbaProb_lineEdit.setObjectName("liczbaProb_lineEdit")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(450, 120, 23, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(430, 150, 38, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Main)
        self.label_6.setGeometry(QtCore.QRect(350, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Main)
        self.label_7.setGeometry(QtCore.QRect(310, 260, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Main)
        self.label_5.setGeometry(QtCore.QRect(310, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_1 = QtWidgets.QLabel(Main)
        self.label_1.setGeometry(QtCore.QRect(400, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.result_pushButton = QtWidgets.QPushButton(Main, clicked=lambda: self.openWindow())
        self.result_pushButton.setGeometry(QtCore.QRect(630, 560, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_pushButton.setFont(font)
        self.result_pushButton.setObjectName("result_pushButton")
        self.ifDone_label = QtWidgets.QLabel(Main)
        self.ifDone_label.setGeometry(QtCore.QRect(100, 530, 491, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ifDone_label.setFont(font)
        self.ifDone_label.setText("")
        self.ifDone_label.setObjectName("ifDone_label")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.uruchom_pushButton.setText(_translate("Main", "Uruchom"))
        self.gra_comboBox.setItemText(0, _translate("Main", "Cart Pole"))
        self.gra_comboBox.setItemText(1, _translate("Main", "Car Racing"))
        self.gra_comboBox.setItemText(2, _translate("Main", "Taxi"))
        self.agent_comboBox.setItemText(0, _translate("Main", "DQN"))
        self.agent_comboBox.setItemText(1, _translate("Main", "A2C"))
        self.agent_comboBox.setItemText(2, _translate("Main", "PPO"))
        self.label_3.setText(_translate("Main", "Gra"))
        self.label_4.setText(_translate("Main", "Agent"))
        self.label_6.setText(_translate("Main", "Współczynnik uczenia "))
        self.label_7.setText(_translate("Main", "Współczynnik dyskontowania"))
        self.label_5.setText(_translate("Main", "Wartość poczatkowa epsilon "))
        self.label_1.setText(_translate("Main", "Liczba prób"))
        self.result_pushButton.setText(_translate("Main", "Pokaż wyniki"))
        self.wspolczynnikUczenia_lineEdit.setText(_translate("Main", "0.3"))
        self.wspolczynnikDyskontowania_lineEdit.setText(_translate("Main", "0.3"))
        self.epsilon_lineEdit.setText(_translate("Main", "0.5"))
        self.liczbaProb_lineEdit.setText(_translate("Main", "100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
