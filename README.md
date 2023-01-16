# Projeto de Urna Eletrônica do CEIT
## Conteudo
1. [Resumo](#resumo)
2. [Descrição geral](#descrição-geral)
3. [FAQ](#faq)
4. [Licença](#licença)
5. [Créditos](#créditos)

### Resumo:

Em resumo, o código cria uma interface gráfica de usuário para uma urna eletrônica usando a biblioteca PyQt6. Ele verifica a entrada do usuário, valida o token, verifica se o token já foi usado e toma ações apropriadas, como abrir a tela de voto ou a tela de resultados. Ele também usa uma classe personalizada DbConect para se conectar ao banco de dados e ler informações do banco de dados. E classes personalizadas para exibir telas de alerta de bloqueio e tela de informações. Este projeto foi desenvolvido por duas pessoas, mais como intuito de aprendizado e "ignorando" algumas boas práticas de segurança (o histórico dos commits é um ótimo exemplo disso).
 
### Descrição geral:

O código acima é um script Python que utiliza a biblioteca PyQt6 para criar uma interface gráfica de usuário (GUI) para uma urna eletrônica. Ele importa várias bibliotecas, como sys, pandas e PyQt6, e também importa três arquivos de código personalizados: db_conector, alerta_bloqueio e tela_informacoes.

A classe MainWindow é a classe principal do script e cria uma janela da urna eletrônica. Ela tem três métodos principais: valida_token, busca_token e login.

O método valida_token verifica se o token inserido pelo usuário existe em uma lista de tokens. Se encontrado, ele imprime o nome e a turma do aluno correspondente ao token e retorna verdadeiro.

O método busca_token verifica se o token inserido já foi usado para votar. Se sim, retorna verdadeiro. Caso contrário, retorna falso.

O método login é responsável por verificar a entrada do usuário e tomar ações apropriadas. Ele verifica se o usuário inseriu um token válido, se o token já foi usado, e se o usuário é o administrador. Se as condições forem atendidas, ele abre a tela de voto ou a tela de resultados. Caso contrário, ele exibe uma mensagem de erro e conta as tentativas de login.

O script também tem dois métodos adicionais chama_alerta_bloqueio e chama_tela_voto, que abrem as telas de alerta de bloqueio e voto, respectivamente.

As variáveis self.tentativas, self.ui_alerta_bloqueio.bloqueado, self.tela_resultados_preenchida são usadas para controlar o número de tentativas de login, se o usuário foi bloqueado, e se a tela de resultados já foi preenchida.

A classe DbConect é importada de db_conector e é usada para se conectar ao banco de dados e ler informações do banco de dados.

As classes Ui_alerta_bloqueio e Ui_Informacoes são importadas de alerta_bloqueio e tela_informacoes, respectivamente e são usadas para criar as telas de alerta de bloqueio e tela de informações.

### FAQ

1. O que é o código acima?
R: O código acima é um script Python que utiliza a biblioteca PyQt6 para criar uma interface gráfica de usuário (GUI) para uma urna eletrônica. Ele verifica a entrada do usuário, valida o token, verifica se o token já foi usado e toma ações apropriadas, como abrir a tela de voto ou a tela de resultados.

2. Como o código valida o token inserido pelo usuário?
R: O código valida o token inserido pelo usuário chamando o método valida_token, que verifica se o token inserido existe em uma lista de tokens. Se encontrado, ele imprime o nome e a turma do aluno correspondente ao token e retorna verdadeiro.

3. Como o código verifica se o token já foi usado?
R: O código verifica se o token já foi usado chamando o método busca_token, que verifica se o token inserido já foi usado para votar. Se sim, retorna verdadeiro. Caso contrário, retorna falso.

4. O que acontece se o usuário inserir um token inválido?
R: Se o usuário inserir um token inválido, o código exibirá uma mensagem de erro e contará a tentativa de login. Se o usuário inserir um token inválido em mais de três tentativas, o código abrirá a tela de alerta de bloqueio.

5. Como o código se conecta ao banco de dados?
R: O código se conecta ao banco de dados usando a classe DbConect, que é importada de db_conector. Esta classe é usada para se conectar ao banco de dados e ler informações do banco de dados.

6. Como o código abre a tela de resultados?
R: O código abre a tela de resultados chamando o método chama_tela_resultados, que verifica se a tela já está preenchida. Se sim, exibe a tela. Se não, preenche a tela antes de exibi-la.

7. Como o código trata a segurança dos dados?
R: O código possui algumas medidas de segurança, como verificar a validade do token inserido pelo usuário e verificar se o token já foi usado. Além disso, o token para o administrador é "4DM1NS3NH400" e ele faz acesso a tela de resultado, isso é uma boa prática de segurança (CONFIA 😆).

8. Como o código trata o bloqueio de usuário?
R: O código trata o bloqueio de usuário contando o número de tentativas de login e, se o usuário inserir um token inválido em mais de três tentativas, o código abre a tela de alerta de bloqueio, impedindo que o usuário faça novas tentativas.

9. Onde posso encontrar mais informações sobre PyQt6 e sua utilização no código?
R: Você pode encontrar mais informações sobre PyQt6 e sua utilização no código visitando o site oficial do PyQt6 (https://www.riverbankcomputing.com/software/pyqt/intro) e lendo a documentação do PyQt6 (https://www.riverbankcomputing.com/static/Docs/PyQt6/).

### Licença

Este código é open-source, ou seja, ele está disponível para qualquer pessoa usar, modificar e distribuir. Isso significa que qualquer pessoa pode baixar o código, alterá-lo para atender às suas necessidades e usá-lo em seus próprios projetos. Porém não pode ser comercializado pois utiliza a biblioteca free do PyQT, e caso queira utilizar em projetos comerciais deve ser comprado a licença no site!

### Créditos

Desenvolvido por:
 - Guilherme Melo de Jesus [Github](https://github.com/Thuripa) [Linkedin](https://www.linkedin.com/in/guilherme-pcguy/)
 - Jackson Luiz Serafim [Github](https://github.com/jacksonserafim) [Linkedin](https://www.linkedin.com/in/jackson-serafim/)
 
 
 
 
 >Parte deste readme foi feito utilizando o ChatGPT com algumas alterações no texto
