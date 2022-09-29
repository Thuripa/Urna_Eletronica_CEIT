import psycopg2


class DbConect:

    # Cria conexão com o banco
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



    def ler_informacao(self):
        DbConect.conectar(self)
        self.cursor.execute('select * from alunos;')

        linhas = self.cursor.fetchall()

        for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Turma: {linha[2]}')
            print("")

    # Função para popular o banco pela 1ª vez
    def popula_banco(self):

        v1 = "aa"
        v2 = "aaa - Teste"
        v3 = "123"

        DbConect.conectar(self)
        print("Populando tabela aluno...")
        self.cursor.execute("INSERT INTO alunos VALUES (%s, %s, %s);", (v1, v2, v3))
        self.cursor.close()
