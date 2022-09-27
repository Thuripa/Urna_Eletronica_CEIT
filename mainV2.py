import sys
import pandas as pd

from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow

from alerta_bloqueio import Ui_alerta_bloqueio


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

    # Verifica se o Token já foi usado
    def busca_token(self, token):
        with open("Recursos/lista_votos.txt", "r") as arquivo:

            # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
            linhas = arquivo.readlines()
            # Busca o Token no registro de votos para saber se já foi usado, retorna TRUE se já foi usado
            for linha in linhas:

                # Se encontrar o Token na lista escreve "- Votou" do lado
                if token.strip() == linha[-13:].strip():
                    print("Token já usado!")
                    arquivo.close()
                    return True

            arquivo.close()
            return False

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

                    self.usuario.setText("Usuário: " + self.input.text())

                    # Abre a tela_resultados
                    self.chama_tela_resultados()

                else:

                    if not self.busca_token(self.input.text()):

                        self.usuario.setText("Usuário: " + self.input.text())

                        # Abre a tela_voto
                        self.chama_tela_voto()

                    else:
                        self.label.setText("Token já utilizado!")

            else:
                print("Token Inválido!")
                self.label.setText("Token Inválido! " + str(self.tentativas + 1) + " de 3 Tentativas...")
                self.tentativas += 1
                print("Tentativas: ", self.tentativas)

    # Exibe Tela Resultados
    def chama_tela_resultados(self):

        # Se a tela já estiver preenchida
        if self.tela_resultados_preenchida:

            # Exibe a Tela
            self.stackedWidget.setCurrentWidget(self.tela_resultados)

        # Senão preenche tela
        else:

            # Preenche Tela Resultados
            self.preenche_tela_resultados()

            # Exibe a Tela
            self.stackedWidget.setCurrentWidget(self.tela_resultados)

    # Preenche a Tela Resultados
    def preenche_tela_resultados(self):

        # A contagem de votos retorna uma lista[] onde: [0] - voto em branco; [1] - chapa 1 ...

        self.tela_resultados_preenchida = True

        # Inicia a lista
        total_votos = [0, 0, 0, 0]

        # Lê o primeiro caracter de cada linha da lista_votos
        with open("Recursos/lista_votos.txt", "r") as arquivo:

            # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
            linhas = arquivo.readlines()

            # Para cada linha do arquivo:
            for linha in linhas:

                # Pega número da chapa
                num_voto = int(linha[0])

                # Adiciona os votos na lista
                if num_voto == 0:
                    total_votos[num_voto] += 1
                if num_voto == 1:
                    total_votos[num_voto] += 1
                if num_voto == 2:
                    total_votos[num_voto] += 1
                if num_voto == 3:
                    total_votos[num_voto] += 1

        # Atualiza os label da tela com o valor dos votos
        self.label_votos_chapa_1.setText(self.label_votos_chapa_1.text() + str(total_votos[1])+" votos")
        self.label_votos_chapa_2.setText(self.label_votos_chapa_2.text() + str(total_votos[2])+" votos")
        self.label_votos_chapa_3.setText(self.label_votos_chapa_3.text() + str(total_votos[3])+" votos")

        # Confere o vencedor e Exibe na Tela

        vencedor = 0

        for x in range(1, len(total_votos)):

            if total_votos[x] > vencedor:
                vencedor = x

        self.label_vencedor.setText("Vencedor: Chapa " + str(vencedor))

    # Exibe Tela Voto
    def chama_tela_voto(self):

        self.stackedWidget.setCurrentWidget(self.tela_voto)

        # Se usuário clicar em 'próximo' na tela voto
        self.btn_chapa.clicked.connect(self.escolhe_chapa)

    # Captura a chapa escolhida na tela voto
    def escolhe_chapa(self):

        chapa = -1

        # Confere qual opção foi escolhida
        if self.rb_chapa1.isChecked():
            chapa = 1
        elif self.rb_chapa2.isChecked():
            chapa = 2
        elif self.rb_chapa3.isChecked():
            chapa = 3
        elif self.rb_branco.isChecked():
            chapa = 0

        self.chama_tela_confirmacao(chapa)

    def get_chapa(self):

        chapa = -1

        # Confere qual opção foi escolhida
        if self.rb_chapa1.isChecked():
            chapa = 1
        elif self.rb_chapa2.isChecked():
            chapa = 2
        elif self.rb_chapa3.isChecked():
            chapa = 3
        elif self.rb_branco.isChecked():
            chapa = 0

        return chapa


    def chama_tela_confirmacao(self, chapa):

        if chapa == -1:
            print("Escolha uma opção!")
        else:

            # Pega o valor do token
            token = self.input.text()

            self.usuario.setText(self.usuario.text() + token)

            # Invoca o método para preencher a tela
            self.preenche_tela_confirmacao(token, chapa)

            # Exibe Janela
            self.stackedWidget.setCurrentWidget(self.tela_confirmacao)

            # Se o usuário clicar em 'cancelar' na tela confirmacao
            self.btn_cancelar.clicked.connect(self.chama_tela_voto)

            # Se o usuário clicar em 'votar' na tela confirmacao
            self.btn_votar.clicked.connect(self.votar)

    def preenche_tela_confirmacao(self, token, num_voto):

        # Se o voto não for branco carrega os nomes da tabela
        if not num_voto == 0:

            # Leitura da tabela alunos_chapa
            alunos_chapa = pd.read_excel('Recursos\\alunos_chapa.xlsx', engine='openpyxl', sheet_name=(num_voto - 1))

            self.label_presidente.setText(f"Presidente: {alunos_chapa.iloc[0, 0]}")
            self.label_sec_geral.setText(f"Secretário Geral: {alunos_chapa.iloc[2, 0]}")
            self.label_1_sec.setText(f"1º Secretário: {alunos_chapa.iloc[3, 0]}")
            self.label_tes_geral.setText(f"Tesoureiro Geral: {alunos_chapa.iloc[4, 0]}")
            self.label_1_tes.setText(f"1º Tesoureiro: {alunos_chapa.iloc[5, 0]}")
            self.label_dir_pedagogico.setText(f"Diretor Pedagógico:{alunos_chapa.iloc[6, 0]}")
            self.label_dir_cultura.setText(f"Diretor de Cultura: {alunos_chapa.iloc[7, 0]}")
            self.label_vice_presidente.setText(f"Vice-Presidente: {alunos_chapa.iloc[1, 0]}")
            self.label_dir_social.setText(f"Diretor Social: {alunos_chapa.iloc[9, 0]}")
            self.label_dir_imprensa.setText(f"Diretor de Imprensa: {alunos_chapa.iloc[8, 0]}")
            self.label_2_suplente.setText(f"2º Suplente: {alunos_chapa.iloc[12, 0]}")
            self.label_1_suplente.setText(f"1º Suplente: {alunos_chapa.iloc[11, 0]}")
            self.label_dir_esporte.setText(f"Diretor de Esporte: {alunos_chapa.iloc[10, 0]}")
            self.usuario.setText("Usuário: " + token)


        else:
            # Não preenche nada...
            pass

    def registra_voto(self, num_voto):

        token = self.input.text()

        with open("Recursos/lista_votos.txt", "a") as arquivo:

            print("Registra voto do Token:", token, "para a chapa: ", str(num_voto))

            # Escreve no arquivo o número da chapa e o token
            arquivo.write(str(num_voto) + " " + token + "\n")

            arquivo.close()

        # Chama tela final
        self.stackedWidget.setCurrentWidget(self.tela_final)

    # Registra voto
    def votar(self):

        # Invonca método registra voto passando a chapa como argumento
        self.registra_voto(self.get_chapa())

    # Bloqueia tela
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

    # Retorna à tela inicial
    def finalizar(self):

        self.stackedWidget.setCurrentIndex(0)

    # Construtor Janela
    def __init__(self):

        # Carrega interface
        super(MainWindow, self).__init__()
        loadUi('UI\\urnav2.ui', self)

        self.tela_inicial = MainWindow

        self.usuario.setText("Usuário: ")

        # Se usuário clicar em 'próximo' na tela inicial
        self.btn_login.clicked.connect(self.login)

        # Se usuário clicar em 'finalizar' na tela resultados
        self.btn_finalizar_resultados.clicked.connect(self.finalizar)


        # Variável para contar tentativas
        self.tentativas = 0

        # Variável para controle da tela_resultados
        self.tela_resultados_preenchida = False

        # Exibe Janela
        self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
