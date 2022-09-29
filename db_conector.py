import psycopg2
import self


class DbConect:

    # Cria conexão com o banco
    def __init__(self):
        self.conectar = None

    def conectar(self):

        # Cria uma conexão com o banco de dados
        self.conectar = psycopg2.connect(
            host='ec2-52-201-124-168.compute-1.amazonaws.com',
            database='d7r4ff1hb1illg',
            user='lqmxqsebbogrfq',
            port=5432,
            password='07d06f38ce7360ba18b365696501ab3e5416990c6f281bf3b2084032d142df8a')

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

        # O problema esta aqui em algum ponto...
        DbConect.conectar(self)
        self.cursor.execute(f'select {coluna} from {tabela};')

        linhas = self.cursor.fetchall()

        '''for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Turma: {linha[2]}')
            print("")'''

        DbConect.fechar_conexao(self)
        return linhas

    # Função para popular o banco pela 1ª vez
    def popula_banco(self, v1, v2, v3):

        DbConect.conectar(self)
        print("Populando tabela aluno...")
        self.cursor.execute("INSERT INTO alunos VALUES (%s, %s, %s);", (v1, v2, v3))
        self.conectar.commit()
        DbConect.fechar_conexao(self)

    def registra_voto(self, token, voto):

        DbConect.conectar(self)
        self.cursor.execute('INSERT INTO votos VALUES (%s, %s);', (token, voto))
        self.conectar.commit()
        DbConect.fechar_conexao(self)

    def fechar_conexao(self):

        # Fecha tudo que é necessario
        self.cursor.close()
        self.conectar.close()

        if self.conectar.closed != 0:
            print('Desconectado com sucesso')
        else:
            print('Deu ruim :(')


