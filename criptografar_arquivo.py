import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def hash_senha():
    #Gera a senha de criptografia baseado em SHA256
    password = input('Senha: ').encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'None',
        iterations=390000,
    )
    chave = base64.urlsafe_b64encode(kdf.derive(password))

    return chave


def criptografar(password):
    #Criptografa cada arquivo do diretório definido (neste caso o Recursos que possuí informações 'sensiveis')
    for file in os.listdir('Recursos'):
        with open(f'Recursos\\{file}', 'rb') as arquivo:
            descripto = arquivo.read()

        cripto = Fernet(password).encrypt(descripto)

        with open(f'Recursos\\{file}', 'wb') as arquivo_crypto:
            arquivo_crypto.write(cripto)


def descriptografar(password):
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
        criptografar(password)
    else:
        descriptografar(password)


if __name__ == '__main__':
    senha = hash_senha()
    escolha_funcao(senha)
