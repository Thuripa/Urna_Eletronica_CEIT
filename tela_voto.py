# Form implementation generated from reading ui file 'C:\Users\Guilherme\PycharmProjects\Urna_Eletronica_CEIT\UI\tela_voto.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import time
from PyQt6 import QtCore, QtGui, QtWidgets
from tela_confirmacao import Ui_tela_confirmacao
from tela_final import Ui_tela_final

class Ui_tela_voto(object):

    # Função que implementa a ação de clicar no botão
    def clicou(self):

        chapa = -1

        # Confere qual opção foi escolhida
        if self.radioButton_1.isChecked():
            chapa = 1
        elif self.radioButton_2.isChecked():
            chapa = 2
        elif self.radioButton_3.isChecked():
            chapa = 3
        elif self.radioButton_4.isChecked():
            chapa = 0

        # Abre tela_confirmacao
        self.chama_tela_confirmacao(chapa)

    # Função que chama a tela_confirmacao
    def chama_tela_confirmacao(self, chapa):

        if chapa == -1:
            print("Escolha uma opção!")
        else:

            # Registra Voto em Branco
            if chapa == 0:

                print("Escolheu Votar em Branco")

                # Chama Tela Final
                self.tela_final = QtWidgets.QDialog()
                self.ui = Ui_tela_final()
                self.ui.setupUi(self.tela_final, self.tela_inicial)
                self.tela_final.show()
                self.tela_voto.close()


            # Chama tela_confirmacao
            else:

                # Cria Janela
                self.tela_confirmacao = QtWidgets.QDialog()
                # Cria Interface
                self.ui = Ui_tela_confirmacao()
                # Chama o Método de "inflar" a interface
                self.ui.setupUi(self.tela_voto, self.tela_confirmacao, self.tela_inicial)

                # Passa o Token como parâmetro para a tela_confirmacao

                # Pega o valor do token do lbl_usuario (os 12 últimos caracteres)
                token = self.lbl_usuario.text()
                token = token[-13:]
                print("Token: ", token)

                self.ui.lbl_usuario.setText(self.ui.lbl_usuario.text()+token)


                # Passa o número da chapa como parâmetro para a tela_confirmacao
                self.ui.lbl_chapa.setText(self.ui.lbl_chapa.text()+str(chapa))
                # Invoca o método para preencher a tela
                self.ui.preenche_tela(token, chapa)

                # Exibe Janela
                self.tela_confirmacao.show()




    def setupUi(self, tela_voto, tela_inicial):

        self.tela_voto = tela_voto
        self.tela_inicial = tela_inicial

        tela_voto.setObjectName("tela_voto")
        tela_voto.resize(866, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        tela_voto.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        tela_voto.setWindowIcon(icon)
        self.titulo = QtWidgets.QLabel(tela_voto)
        self.titulo.setGeometry(QtCore.QRect(290, 30, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(tela_voto)
        self.label.setGeometry(QtCore.QRect(290, 120, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn = QtWidgets.QPushButton(tela_voto)
        self.btn.setGeometry(QtCore.QRect(290, 500, 231, 71))
        self.btn.clicked.connect(self.clicou)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.logo = QtWidgets.QLabel(tela_voto)
        self.logo.setGeometry(QtCore.QRect(10, 10, 230, 230))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.radioButton_1 = QtWidgets.QRadioButton(tela_voto)
        self.radioButton_1.setGeometry(QtCore.QRect(290, 200, 450, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(tela_voto)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 270, 450, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(tela_voto)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 340, 450, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(tela_voto)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 410, 450, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lbl_usuario = QtWidgets.QLabel(tela_voto)
        self.lbl_usuario.setGeometry(QtCore.QRect(20, 280, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setObjectName("label_2")

        self.retranslateUi(tela_voto)
        QtCore.QMetaObject.connectSlotsByName(tela_voto)

    def retranslateUi(self, tela_voto):
        _translate = QtCore.QCoreApplication.translate
        tela_voto.setWindowTitle(_translate("tela_voto", "URNA CEIT"))
        self.titulo.setText(_translate("tela_voto", "ELEIÇÕES GRÊMIO ESTUDANTIL CEIT - 2022"))
        self.label.setText(_translate("tela_voto", "Escolha a chapa em que deseja votar:"))
        self.btn.setText(_translate("tela_voto", "Próximo"))
        self.radioButton_1.setText(_translate("tela_voto", "Chapa 1"))
        self.radioButton_2.setText(_translate("tela_voto", "Chapa 2"))
        self.radioButton_3.setText(_translate("tela_voto", "Chapa 3"))
        self.radioButton_4.setText(_translate("tela_voto", "Branco"))
        self.lbl_usuario.setText(_translate("tela_voto", "Usuário: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_voto = QtWidgets.QDialog()
    ui = Ui_tela_voto()
    ui.setupUi(tela_voto)
    tela_voto.show()
    sys.exit(app.exec())
