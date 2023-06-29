import psycopg2
import self
import pandas as pd


class DbConect:
    # Cria conexão com o banco
    def conectar(self):

        # Cria uma conexão com o banco de dados
        self.conectar = psycopg2.connect(
            host='',
            database='',
            user='',
            port=,
            password='')

        # Cria um "garçom" kkk
        self.cursor = self.conectar.cursor()

        # Checa se está conectado
        if self.conectar.closed == 0:
            print('Conectado com sucesso')
        else:
            print('Desconectado do servidor')

        # Versão do servidor
        db_info = self.conectar.server_version
        print(f'Versão do servidor: {db_info}')

    def ler_informacao(self, coluna, tabela):

        self.cursor.execute(f'select {coluna} from {tabela};')

        linhas = self.cursor.fetchall()

        '''for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Turma: {linha[2]}')
            print("")'''

        return linhas

    # Insere aluno no banco
    def insere_aluno(self, token, nome, turma):

        print("Populando tabela aluno...")

        self.cursor.execute("INSERT INTO alunos VALUES (%s, %s, %s);", (token, nome, turma))

        self.conectar.commit()

    # Registra o voto no banco
    def registra_voto(self, token, voto):

        self.cursor.execute(f'INSERT INTO votos VALUES (%s, %s);', (token, voto))
        self.conectar.commit()

    # Encerra conexão
    def fechar_conexao(self):

        # Fecha tudo que é necessario
        self.cursor.close()
        self.conectar.close()

        if self.conectar.closed != 0:
            print('Desconectado com sucesso')
        else:
            print('Deu ruim :(')


