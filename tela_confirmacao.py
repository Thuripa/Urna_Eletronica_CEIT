# Form implementation generated from reading ui file 'C:\Users\Guilherme\PycharmProjects\Urna_Eletronica_CEIT\UI\tela_confirmacao_2.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from tela_final import Ui_tela_final


class Ui_tela_confirmacao(object):

    # Preenche a tela de acordo com a chapa escolhida
    def preenche_tela(self, token,num_voto):

        # Leitura da tabela da chapa
        alunos_chapa = pd.read_excel('Recursos\\alunos_chapa.xlsx', engine='openpyxl', sheet_name=(num_voto-1))

        self.titulo.setText("ELEIÇÕES GRÊMIO ESTUDANTIL CEIT - 2022")
        self.label.setText("Deseja Confirmar Seu Voto?")
        self.btn_cancelar.setText("Cancelar")
        self.btn_votar.setText("Votar")
        self.lbl_presidente.setText(f"Presidente: {alunos_chapa.iloc[0, 0]}")
        self.lbl_sec_geral.setText(f"Secretário Geral: {alunos_chapa.iloc[2, 0]}")
        self.lbl_1_sec.setText(f"1º Secretário: {alunos_chapa.iloc[3, 0]}")
        self.lbl_tes_geral.setText(f"Tesoureiro Geral: {alunos_chapa.iloc[4, 0]}")
        self.lbl_1_tes.setText(f"1º Tesoureiro: {alunos_chapa.iloc[5, 0]}")
        self.lbl_dir_pedagogico.setText(f"Diretor Pedagógico:{alunos_chapa.iloc[6, 0]}")
        self.lbl_dir_cultura.setText(f"Diretor de Cultura: {alunos_chapa.iloc[7, 0]}")
        self.lbl_vice_pres.setText(f"Vice-Presidente: {alunos_chapa.iloc[1, 0]}")
        self.lbl_dir_social.setText(f"Diretor Social: {alunos_chapa.iloc[9, 0]}")
        self.lbl_dir_imprensa.setText(f"Diretor de Imprensa: {alunos_chapa.iloc[8, 0]}")
        self.lbl_2_suplente.setText(f"2º Suplente: {alunos_chapa.iloc[12, 0]}")
        self.lbl_1_suplente.setText(f"1º Suplente: {alunos_chapa.iloc[11, 0]}")
        self.lbl_dir_esporte.setText(f"Diretor de Esporte: {alunos_chapa.iloc[10, 0]}")
        self.lbl_usuario.setText("Usuário: "+token)
        self.lbl_chapa.setText("Chapa:  "+str(num_voto))


    # Registra Voto em um arquivo e soma o total de votos
    def acao_btn_votar(self):

        token = self.lbl_usuario.text()
        token = token[-13:]
        print("Token 2: ", token)

        chapa = self.lbl_chapa.text()[-1]

        # Registra Voto num arquivo
        with open("Recursos/lista_votos.txt", "a") as arquivo:

            # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
            arquivo.write(chapa+token+"\n")

            arquivo.close()

        # Fecha a tela_voto
        self.tela_voto.close()

        # Chama Tela Final
        self.tela_final = QtWidgets.QDialog()
        self.ui = Ui_tela_final()
        self.ui.setupUi(self.tela_final, self.tela_inicial)
        self.tela_final.show()
        self.tela_confirmacao.close()


    def setupUi(self, tela_voto, tela_confirmacao, tela_inicial):

        self.tela_voto = tela_voto
        self.tela_confirmacao = tela_confirmacao
        self.tela_inicial = tela_inicial

        larguraLabel = 550


        tela_confirmacao.setObjectName("Tela Confirmação")
        tela_confirmacao.resize(1080, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        tela_confirmacao.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        tela_confirmacao.setWindowIcon(icon)
        self.titulo = QtWidgets.QLabel(tela_confirmacao)
        self.titulo.setGeometry(QtCore.QRect(290, 30, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(tela_confirmacao)
        self.label.setGeometry(QtCore.QRect(290, 90, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_cancelar = QtWidgets.QPushButton(tela_confirmacao)
        self.btn_cancelar.setGeometry(QtCore.QRect(290, 520, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_cancelar.clicked.connect(tela_confirmacao.close)
        self.logo = QtWidgets.QLabel(tela_confirmacao)
        self.logo.setGeometry(QtCore.QRect(10, 10, 230, 230))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.btn_votar = QtWidgets.QPushButton(tela_confirmacao)
        self.btn_votar.setGeometry(QtCore.QRect(680, 520, 231, 71))
        self.btn_votar.clicked.connect(self.acao_btn_votar)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_votar.setFont(font)
        self.btn_votar.setObjectName("btn_votar")
        self.lbl_presidente = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_presidente.setGeometry(QtCore.QRect(290, 160, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_presidente.setFont(font)
        self.lbl_presidente.setObjectName("lbl_presidente")
        self.lbl_sec_geral = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_sec_geral.setGeometry(QtCore.QRect(290, 210, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_sec_geral.setFont(font)
        self.lbl_sec_geral.setObjectName("lbl_sec_geral")
        self.lbl_1_sec = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_1_sec.setGeometry(QtCore.QRect(680, 260, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_1_sec.setFont(font)
        self.lbl_1_sec.setObjectName("lbl_1_sec")
        self.lbl_tes_geral = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_tes_geral.setGeometry(QtCore.QRect(290, 260, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_tes_geral.setFont(font)
        self.lbl_tes_geral.setObjectName("lbl_tes_geral")
        self.lbl_1_tes = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_1_tes.setGeometry(QtCore.QRect(680, 320, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_1_tes.setFont(font)
        self.lbl_1_tes.setObjectName("lbl_1_tes")
        self.lbl_dir_pedagogico = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_dir_pedagogico.setGeometry(QtCore.QRect(290, 310, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dir_pedagogico.setFont(font)
        self.lbl_dir_pedagogico.setObjectName("lbl_dir_pedagogico")
        self.lbl_dir_cultura = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_dir_cultura.setGeometry(QtCore.QRect(680, 370, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dir_cultura.setFont(font)
        self.lbl_dir_cultura.setObjectName("lbl_dir_cultura")
        self.lbl_vice_pres = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_vice_pres.setGeometry(QtCore.QRect(680, 210, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_vice_pres.setFont(font)
        self.lbl_vice_pres.setObjectName("lbl_vice_pres")
        self.lbl_dir_social = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_dir_social.setGeometry(QtCore.QRect(680, 430, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dir_social.setFont(font)
        self.lbl_dir_social.setObjectName("lbl_dir_social")
        self.lbl_dir_imprensa = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_dir_imprensa.setGeometry(QtCore.QRect(290, 360, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dir_imprensa.setFont(font)
        self.lbl_dir_imprensa.setObjectName("lbl_dir_imprensa")
        self.lbl_2_suplente = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_2_suplente.setGeometry(QtCore.QRect(680, 480, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_2_suplente.setFont(font)
        self.lbl_2_suplente.setObjectName("lbl_2_suplente")
        self.lbl_1_suplente = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_1_suplente.setGeometry(QtCore.QRect(290, 460, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_1_suplente.setFont(font)
        self.lbl_1_suplente.setObjectName("lbl_1_suplente")
        self.lbl_dir_esporte = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_dir_esporte.setGeometry(QtCore.QRect(290, 410, larguraLabel, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dir_esporte.setFont(font)
        self.lbl_dir_esporte.setObjectName("lbl_dir_esporte")
        self.lbl_usuario = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_usuario.setGeometry(QtCore.QRect(10, 270, larguraLabel, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.lbl_chapa = QtWidgets.QLabel(tela_confirmacao)
        self.lbl_chapa.setGeometry(QtCore.QRect(10, 330, larguraLabel, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lbl_chapa.setFont(font)
        self.lbl_chapa.setObjectName("lbl_chapa")

        self.retranslateUi(tela_confirmacao)
        QtCore.QMetaObject.connectSlotsByName(tela_confirmacao)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "URNA CEIT"))
        self.titulo.setText(_translate("Dialog", "ELEIÇÕES GRÊMIO ESTUDANTIL CEIT - 2022"))
        self.label.setText(_translate("Dialog", "Deseja Confirmar Seu Voto?"))
        self.btn_cancelar.setText(_translate("Dialog", "Cancelar"))
        self.btn_votar.setText(_translate("Dialog", "Votar"))
        self.lbl_presidente.setText(_translate("Dialog", f"Presidente: "))
        self.lbl_sec_geral.setText(_translate("Dialog", f"Secretário Geral: "))
        self.lbl_1_sec.setText(_translate("Dialog", f"1º Secretário: "))
        self.lbl_tes_geral.setText(_translate("Dialog", f"Tesoureiro Geral: "))
        self.lbl_1_tes.setText(_translate("Dialog", f"1º Tesoureiro: "))
        self.lbl_dir_pedagogico.setText(_translate("Dialog", f"Diretor Pedagógico:"))
        self.lbl_dir_cultura.setText(_translate("Dialog", f"Diretor de Cultura: "))
        self.lbl_vice_pres.setText(_translate("Dialog", f"Vice-Presidente: "))
        self.lbl_dir_social.setText(_translate("Dialog", f"Diretor Social: "))
        self.lbl_dir_imprensa.setText(_translate("Dialog", f"Diretor de Imprensa: "))
        self.lbl_2_suplente.setText(_translate("Dialog", f"2º Suplente: "))
        self.lbl_1_suplente.setText(_translate("Dialog", f"1º Suplente: "))
        self.lbl_dir_esporte.setText(_translate("Dialog", f"Diretor de Esporte: "))
        self.lbl_usuario.setText(_translate("Dialog", "Usuário: "))
        self.lbl_chapa.setText(_translate("Dialog", "Chapa:  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_confirmacao = QtWidgets.QDialog()
    ui = Ui_tela_confirmacao()
    ui.setupUi(tela_confirmacao)
    tela_confirmacao.show()
    sys.exit(app.exec())
