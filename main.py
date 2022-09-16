# Projeto Urna CEIT

def valida_token():
    # Atribui o arquivo txt com os tokens para a variável arquivo
    with open("lista_tokens.txt", "r") as arquivo:

        # Linhas é uma lista[] onde cada elemento é uma linha do arquivo
        linhas = arquivo.readlines()

        # Percorre Linhas
        for linha in linhas:
            # Se encontrar o token inserido pelo usuário dentro da lista de tokens retorna verdadeiro
            if usuario in linha:
                arquivo.close()
                return True
        arquivo.close()
        return False



usuario = input("Insira seu Token de Aluno: ")

if valida_token():
    print("Usuário Encontrado!")
else:
    print("Usuário Inexistente!")

