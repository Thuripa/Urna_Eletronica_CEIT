import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow

from alerta_bloqueio import Ui_alerta_bloqueio
from tela_resultados import Ui_tela_resultados


# Janela Urna
class MainWindow(QMainWindow):

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

    def login(self):

        # Se o alerta já tiver sido gerado e a senha já tiver sido inserida corretamente
        if self.tentativas == 99 and self.ui_alerta_bloqueio.bloqueado == False:

            # Zera o número de tentativas
            self.tentativas = 0

        # Senão, se tentativas restantes acabarem exibe o alerta de bloqueio
        elif self.tentativas >= 3:
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
                    self.hide()
                else:

                    if not self.busca_token(self.input.text()):
                        # Abre a tela_voto
                        self.chama_tela_voto()

                        # Esconde a tela atual
                        self.hide()
                    else:
                        self.label.setText("Token já utilizado!")

            else:
                print("Token Inválido!")
                self.label.setText("Token Inválido! " + str(self.tentativas + 1) + " de 3 Tentativas...")
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
        self.hide()

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

    # Construtor Janela
    def __init__(self):

        # Carrega interface
        super(MainWindow, self).__init__()
        loadUi('UI\\urnav2.ui', self)

        self.tela_inicial = MainWindow

        # Se usuário clicar em 'próximo' na tela inicial
        self.btn_login.clicked.connect(self.login)

        # Variável para contar tentativas
        self.tentativas = 0

        # Exibe Janela
        self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
