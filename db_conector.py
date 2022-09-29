import psycopg2

class DbConect:

    def conectar():
        host = 'ec2-52-201-124-168.compute-1.amazonaws.com'
        db = 'd7r4ff1hb1illg'
        user = 'lqmxqsebbogrfq'
        senha = '07d06f38ce7360ba18b365696501ab3e5416990c6f281bf3b2084032d142df8a'
        conectar = psycopg2.connect(host=host, database=db, user=user, port=5432, password=senha)
        cursor = conectar.cursor()

        print(conectar.closed)
        db_info = conectar.server_version
        print(db_info)
        cursor.execute('select * from alunos;')
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f'Token: {linha[0]}')
            print(f'Aluno: {linha[1]}')
            print(f'Serie: {linha[2]}')

        cursor.close()
        conectar.close()

        print(conectar.closed)


if __name__ == '__main__':
    DbConect.conectar()
