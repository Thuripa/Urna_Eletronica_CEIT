# Projeto Urna CEIT
import sys


# Função Que busca o Token na Lista
def valida_token():
    # Atribui o arquivo txt com os tokens para a variável arquivo
    with open("lista_tokens.txt", "r") as arquivo:

        # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
        linhas = arquivo.readlines()

        # Se encontrar o token inserido pelo usuário dentro da lista de tokens retorna VERDADEIRO e fecha o arquivo
        for linha in linhas:
            if usuario == linha.strip():
                arquivo.close()
                return True
            else:
                print(usuario, " != ", linha.strip())

        # Se não encontrar o token retorna FALSO e fecha o arquivo
        arquivo.close()
        return False


# Entrada do usuário (No caso seria o texto de um objeto da UI)
usuario = input("Insira seu Token de Aluno: ")


if valida_token():
    print("Usuário Encontrado!")
else:
    print("Usuário Inexistente!")
