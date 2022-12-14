# Form implementation generated from reading ui file 'C:\Users\Guilherme\PycharmProjects\Urna_Eletronica_CEIT\UI\tela_inicial.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from tela_voto import Ui_tela_voto
from alerta_bloqueio import Ui_alerta_bloqueio
from tela_resultados import Ui_tela_resultados
import criptografar_arquivo


# CLASSE tela_inicial
class Ui_tela_inicial(object):

    # VALIDA TOKEN
    def valida_token(self, token):
        # Atribui o arquivo txt com os tokens para a variável arquivo
        with open("Recursos/lista_tokens.txt", "r") as arquivo:

            # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
            linhas = arquivo.readlines()

            # Se a primeira linha for um Token válido então a lista_tokens está descriptografada
            if linhas[0].strip() == "ZTYyA5zKLtKq":
                print("Arquivo lista_tokens em texto limpo")
                # Se encontrar o token inserido pelo usuário dentro da lista de tokens retorna VERDADEIRO
                for linha in linhas:
                    if token == linha.strip():
                        arquivo.close()
                        return True


    def busca_token(self, token):
        with open("Recursos/lista_votos.txt", "r") as arquivo:

            # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
            linhas = arquivo.readlines()
            # Busca o Token no registro de votos para saber se já foi usado, retorna TRUE se já foi usado
            for linha in linhas:
                print(linha[-13:].strip())
                # Se encontrar o Token na lista escreve "- Votou" do lado
                if token.strip() == linha[-13:].strip():
                    print("Token já usado!")
                    arquivo.close()
                    return True

            arquivo.close()
            return False

    # Função que implementa a ação de clicar no botão
    def clicou(self):

        # Se o alerta já tiver sido gerado e a senha já tiver sido inserida corretamente
        if self.tentativas == 99 and self.ui_alerta_bloqueio.bloqueado == False:

            # Zera o número de tentativas
            self.tentativas = 0

        # senão, se tentativas restantes acabarem exibe o alerta de bloqueio
        elif self.tentativas >=3:
            # Abre alerta_bloqueio
            print("Abre tela_bloqueio")
            self.chama_alerta_bloqueio()

        # Verifica entrada do usuário
        elif self.input.text() == "":
            print("Insira um Token!")
            self.label.setText("Insira um Token!")
        else:
            print("Token: ", self.input.text())

            # Chama função de validação do Token
            if self.valida_token(self.input.text()):
                print("Token Válido!")

                # Se o Token for a senha do admin (boas práticas de segurança foi pro espaço rs)
                if self.input.text().strip() == "4DM1NS3NH400":
                    # Abre a tela_resultados
                    self.chama_tela_resultados()

                    # Esconde a tela atual
                    tela_inicial.hide()
                else:

                    if not self.busca_token(self.input.text()):
                        # Abre a tela_voto
                        self.chama_tela_voto()

                        # Esconde a tela atual
                        tela_inicial.hide()
                    else:
                        self.label.setText("Token já utilizado!")

            else:
                print("Token Inválido!")
                self.label.setText("Token Inválido! "+str(self.tentativas+1)+" de 3 Tentativas...")
                self.tentativas += 1
                print("Tentativas: ", self.tentativas)

    # Exibe Tela Resultados
    def chama_tela_resultados(self):
        # Cria Janela
        self.tela_resultados = QtWidgets.QDialog()
        # Cria Interface
        self.ui = Ui_tela_resultados()
        # Chama o Método de "inflar" a interface na janela passando o token como parâmetro
        self.ui.setupUi(self.tela_resultados, self.tela_inicial)
        # Exibe Janela
        self.tela_resultados.show()
        # Esconde tela_inicial
        tela_inicial.hide()

    # Função que chama a tela_voto
    def chama_tela_voto(self):
        # Cria Janela
        self.tela_voto = QtWidgets.QDialog()
        # Cria Interface
        self.ui = Ui_tela_voto()
        # Chama o Método de "inflar" a interface na janela passando o token como parâmetro
        self.ui.setupUi(self.tela_voto, self.tela_inicial)
        # Passa o Token como parâmetro para a tela_voto
        self.ui.lbl_usuario.setText(self.ui.lbl_usuario.text() + self.input.text())
        # Exibe Janela
        self.tela_voto.show()
        # Esconde tela_inicial
        tela_inicial.hide()

    def chama_alerta_bloqueio(self):

        # Se o número de tentativas for 99 eu sei que alerta já foi acionado
        self.tentativas = 99

        # Cria Janela
        self.alerta_bloqueio = QtWidgets.QDialog()
        # Cria Interface
        self.ui_alerta_bloqueio = Ui_alerta_bloqueio()
        # Chama o Método de "inflar" a interface
        self.ui_alerta_bloqueio.setupUi(self.alerta_bloqueio)
        # Exibe Janela
        self.alerta_bloqueio.show()


        if not self.ui_alerta_bloqueio.bloqueado:
            # Zera as Tentativas
            print("Zerou Tentativas")
            self.tentativas = 0
        else:
            print("bloqueado")

            # Reabre a Janela

            # Cria Janela
            self.alerta_bloqueio = QtWidgets.QDialog()
            # Cria Interface
            self.ui_alerta_bloqueio = Ui_alerta_bloqueio()
            # Chama o Método de "inflar" a interface e passa a janela como parâmetro
            self.ui_alerta_bloqueio.setupUi(self.alerta_bloqueio)
            # Exibe Janela
            self.alerta_bloqueio.show()

        # Restaura label
        self.label.setText("Insira seu Token de aluno:")

    def setupUi(self, tela_inicial):

        # Variável para contar tentativas
        self.tentativas = 0

        # Cria a classe criptografar_arquivo
        self.criptografar_arquivo = criptografar_arquivo

        self.chave = self.criptografar_arquivo.hash_senha()

        # Cria a tela_inicial
        self.tela_inicial = tela_inicial

        tela_inicial.setObjectName("Dialog")
        tela_inicial.resize(866, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        tela_inicial.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        tela_inicial.setWindowIcon(icon)
        self.titulo = QtWidgets.QLabel(tela_inicial)
        self.titulo.setGeometry(QtCore.QRect(290, 30, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(tela_inicial)
        self.label.setGeometry(QtCore.QRect(290, 220, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input = QtWidgets.QLineEdit(tela_inicial)
        self.input.setGeometry(QtCore.QRect(290, 300, 541, 60))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.input.setFont(font)
        self.input.setMaxLength(12)
        self.input.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.input.setObjectName("input")
        self.btn = QtWidgets.QPushButton(tela_inicial)
        self.btn.setGeometry(QtCore.QRect(290, 390, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.clicou)

        self.logo = QtWidgets.QLabel(tela_inicial)
        self.logo.setGeometry(QtCore.QRect(10, 0, 230, 230))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("UI\\Logo CEIT.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.retranslateUi(tela_inicial)
        QtCore.QMetaObject.connectSlotsByName(tela_inicial)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "URNA CEIT"))
        self.titulo.setText(_translate("Dialog", "ELEIÇÕES GRÊMIO ESTUDANTIL CEIT - 2022"))
        self.label.setText(_translate("Dialog", "Insira seu Token de aluno:"))
        self.input.setText(_translate("Dialog", ""))
        self.btn.setText(_translate("Dialog", "Próximo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_inicial = QtWidgets.QDialog()
    ui = Ui_tela_inicial()
    ui.setupUi(tela_inicial)
    tela_inicial.show()
    sys.exit(app.exec())
