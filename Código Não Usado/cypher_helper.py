import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Uma classe helper
class cypher_helper():

    # Retorna Chave
    def get_chave():
        #Gera a senha de criptografia baseado em SHA256
        password = input('Senha: ').encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'None',
            iterations=390000,
        )
        chave = base64.urlsafe_b64encode(kdf.derive(password))

        # Retorna Chave
        return chave


    def criptografar_pasta(chave):
        # Criptografa os arquivos da pasta Recursos
        for file in os.listdir('Recursos'):
            with open(f'Recursos\\{file}', 'rb') as arquivo:
                descripto = arquivo.read()

            cripto = Fernet(chave).encrypt(descripto)

            with open(f'Recursos\\{file}', 'wb') as arquivo_crypto:
                arquivo_crypto.write(cripto)

    def descriptografar_pasta(chave):
        # Descriptografa os arquivos da pasta Recursos
        for file in os.listdir('Recursos'):
            with open(f'Recursos\\{file}', 'rb') as arquivo:
                criptografado = arquivo.read()

            descriptografado = Fernet(chave).decrypt(criptografado)

            with open(f'Recursos\\{file}', 'wb') as arquivo_crypto:
                arquivo_crypto.write(descriptografado)