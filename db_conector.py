import psycopg2


class DbConect:

    # Cria conexão com o banco
    def conectar(self):

        # Define as credenciais do banco
        self.host = 'ec2-52-201-124-168.compute-1.amazonaws.com'
        self.db = 'd7r4ff1hb1illg'
        self.user = 'lqmxqsebbogrfq'
        self.senha = '07d06f38ce7360ba18b365696501ab3e5416990c6f281bf3b2084032d142df8a'

        self.conectar = psycopg2.connect(host=self.host, database=self.db, user=self.user, port=5432, password=self.senha)

        # Criar um 'cursor' com o banco de dados para executar os comando SQL
        self.cursor = self.conectar.cursor()

        # Checa se esta conectado
        if self.conectar.closed == 0:
            print('Conectado com sucesso')

        # Versão do servidor
        db_info = self.conectar.server_version

        print(f'Versão do servidor: {db_info}')

        # Apenas para teste se esta conseguindo pegar as informações
        '''self.cursor.execute('select * from alunos;')

        linhas = self.cursor.fetchall()

        for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Serie: {linha[2]}')

        self.cursor.close()
        self.conectar.close()

        if self.conectar.closed != 0:
            print('Desconectado do servidor')'''

    def ler_informacao(self):
        DbConect.conectar(self)
        self.cursor.execute('select * from alunos;')

        linhas = self.cursor.fetchall()

        for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Serie: {linha[2]}')