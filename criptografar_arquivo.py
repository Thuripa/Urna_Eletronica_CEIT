import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Gera Chave
def hash_senha():
    #Gera a senha de criptografia baseado em SHA256
    password = b"senha"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'None',
        iterations=390000,
    )
    chave = base64.urlsafe_b64encode(kdf.derive(password))

    return chave


# Criptografa um arquivo específico da pasta Recursos
def criptografar_arquivo(password, nome_arquivo):

        with open(f'Recursos\\'+nome_arquivo, 'rb') as arquivo:
            descripto = arquivo.read()

        cripto = Fernet(password).encrypt(descripto)

        with open(f'Recursos\\'+nome_arquivo, 'wb') as arquivo_crypto:
            arquivo_crypto.write(cripto)


# Descriptografa um arquivo específico da pasta Recursos
def descriptografar_arquivo(password, nome_arquivo):
    #Descriptografa os arquivos da pasta Recursos
    for file in os.listdir('Recursos'):
        with open(f'Recursos\\'+nome_arquivo, 'rb') as arquivo:
            criptografado = arquivo.read()

        descriptografado = Fernet(password).decrypt(criptografado)

        with open(f'Recursos\\'+nome_arquivo, 'wb') as arquivo_crypto:
            arquivo_crypto.write(descriptografado)


def criptografar_pasta(password):
    #Criptografa cada arquivo do diretório definido (neste caso o Recursos que possuí informações 'sensiveis')
    for file in os.listdir('Recursos'):
        with open(f'Recursos\\{file}', 'rb') as arquivo:
            descripto = arquivo.read()

        cripto = Fernet(password).encrypt(descripto)

        with open(f'Recursos\\{file}', 'wb') as arquivo_crypto:
            arquivo_crypto.write(cripto)


def descriptografar_pasta(password):
    #Descriptografa os arquivos da pasta Recursos
    for file in os.listdir('Recursos'):
        with open(f'Recursos\\{file}', 'rb') as arquivo:
            criptografado = arquivo.read()

        descriptografado = Fernet(password).decrypt(criptografado)

        with open(f'Recursos\\{file}', 'wb') as arquivo_crypto:
            arquivo_crypto.write(descriptografado)


def escolha_funcao(password):
    escolha = int(input('1 - Criptografar\n2 - Descriptografar\nO que deseja fazer? '))
    if escolha == 1:
        criptografar_pasta(password)
    else:
        descriptografar_pasta(password)


if __name__ == '__main__':
    senha = hash_senha()
    escolha_funcao(senha)
