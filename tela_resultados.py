# Form implementation generated from reading ui file 'C:\Users\Guilherme\PycharmProjects\Urna_Eletronica_CEIT\UI\tela_resultados.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_tela_resultados(object):

    def finalizar(self):

        self.tela_resultados.close()
        self.tela_inicial.show()

    def clicou(self):
        self.finalizar()

    # Contagem de votos
    def conta_votos(self):

        # A contagem de votos retorna uma lista[] onde: [0] - voto em branco; [1] - chapa 1 ...

        # Inicia a lista
        total_votos = [0,0,0,0]

        # Lê o primeiro caracter de cada linha da lista_votos
        with open("Recursos/lista_votos.txt", "r") as arquivo:

            # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
            linhas = arquivo.readlines()

            # Para cada linha do arquivo:
            for linha in linhas:

                # Pega número da chapa
                num_voto = int(linha[0])
                print("Número do Voto: ", num_voto)

                # Adiciona os votos na lista
                if num_voto == 0:
                    total_votos[num_voto] += 1
                if num_voto == 1:
                    total_votos[num_voto] += 1
                if num_voto == 2:
                    total_votos[num_voto] += 1
                if num_voto == 3:
                    total_votos[num_voto] += 1

            arquivo.close()
            return total_votos


    # Preenche a Tela
    def preenche_tela(self):

        total_votos = self.conta_votos()

        self.lblChapa1.setText(self.lblChapa1.text()+str(total_votos[1]))
        self.lblChapa2.setText(self.lblChapa2.text()+str(total_votos[2]))
        self.lblChapa3.setText(self.lblChapa3.text()+str(total_votos[3]))

        # Confere o vencedor e Exibe na Tela

        vencedor = 0

        for x in range(1, len(total_votos)):

            if total_votos[x] > vencedor:
                vencedor = x

        self.lblVencedor.setText("Vencedor: Chapa "+str(vencedor))



    def setupUi(self, tela_resultados, tela_inicial):

        self.tela_resultados = tela_resultados

        self.tela_inicial = tela_inicial

        tela_resultados.setObjectName("Dialog")
        tela_resultados.resize(866, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        tela_resultados.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        tela_resultados.setWindowIcon(icon)
        self.titulo = QtWidgets.QLabel(tela_resultados)
        self.titulo.setGeometry(QtCore.QRect(290, 30, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(tela_resultados)
        self.label.setGeometry(QtCore.QRect(290, 110, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_finalizar = QtWidgets.QPushButton(tela_resultados)
        self.btn_finalizar.setGeometry(QtCore.QRect(600, 500, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_finalizar.setFont(font)
        self.btn_finalizar.setObjectName("btn_finalizar")
        self.btn_finalizar.clicked.connect(self.clicou)
        self.logo = QtWidgets.QLabel(tela_resultados)
        self.logo.setGeometry(QtCore.QRect(10, 0, 230, 230))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.lblChapa1 = QtWidgets.QLabel(tela_resultados)
        self.lblChapa1.setGeometry(QtCore.QRect(290, 270, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblChapa1.setFont(font)
        self.lblChapa1.setObjectName("lblChapa1")
        self.lblChapa2 = QtWidgets.QLabel(tela_resultados)
        self.lblChapa2.setGeometry(QtCore.QRect(290, 330, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblChapa2.setFont(font)
        self.lblChapa2.setObjectName("lblChapa2")
        self.lblChapa3 = QtWidgets.QLabel(tela_resultados)
        self.lblChapa3.setGeometry(QtCore.QRect(290, 390, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblChapa3.setFont(font)
        self.lblChapa3.setObjectName("lblChapa3")
        self.lblVencedor = QtWidgets.QLabel(tela_resultados)
        self.lblVencedor.setGeometry(QtCore.QRect(30, 270, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblVencedor.setFont(font)
        self.lblVencedor.setObjectName("lblVencedor")

        self.retranslateUi(tela_resultados)
        QtCore.QMetaObject.connectSlotsByName(tela_resultados)


        # Preenche Tela
        self.preenche_tela()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "URNA CEIT"))
        self.titulo.setText(_translate("Dialog", "ELEIÇÕES GRÊMIO ESTUDANTIL CEIT - 2022"))
        self.label.setText(_translate("Dialog", "Resultados:"))
        self.btn_finalizar.setText(_translate("Dialog", "Finalizar"))
        self.lblChapa1.setText(_translate("Dialog", "Chapa 1:"))
        self.lblChapa2.setText(_translate("Dialog", "Chapa 2:"))
        self.lblChapa3.setText(_translate("Dialog", "Chapa 3:"))
        self.lblVencedor.setText(_translate("Dialog", "Vencedor: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_resultados = QtWidgets.QDialog()
    ui = Ui_tela_resultados()
    ui.setupUi(tela_resultados)
    tela_resultados.show()
    sys.exit(app.exec())
