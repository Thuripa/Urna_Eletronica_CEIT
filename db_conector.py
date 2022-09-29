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
        self.cursor = self.conectar.cursor()

        print(self.conectar.closed)

        db_info = self.conectar.server_version

        print(db_info)

        self.cursor.execute('select * from alunos;')

        linhas = self.cursor.fetchall()

        for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Serie: {linha[2]}')

        self.cursor.close()
        self.conectar.close()

        print(self.conectar.closed)


if __name__ == '__main__':
    DbConect.conectar()
