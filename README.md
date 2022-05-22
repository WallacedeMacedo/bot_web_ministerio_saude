# bot_web_ministerio_saude
Bot Ministério da Saúde.

Este Bot foi desenvolvido para baixar o arquivo compactado(rar, zip e 7z) no site do Ministério da Saúde. 

Após o download o arquivo é movido do diretório Download para o diretório arquivos/compactados dentro do projeto, em seguida os arquivos são extraidos no 
diretório arquivos/extraidos e carregados no banco de dados oracle.

# Antes de executar o projeto é preciso seguir os passos abaixo.

Após baixar o projeto no github é preciso seguir os passos abaixo.

1º Passo
Instale o cx_Oracle:
python -m pip install cx_Oracle --upgrade --user

2º Passo
As bibliotecas do Oracle Client precisam ser instaladas separadamente. Escolha de acordo com a versão do seu banco de dados.
https://www.oracle.com/br/database/technologies/instant-client/winx64-64-downloads.html

3º Passo
Após baixar e extrair o instantclient, cole dentro do diretório APP do projeto.

4º Passo
Abra o editor de texto ou IDE, de sua preferência, e alterar o arquivo conexao_database.py e informe para cx_Oracle.init_oracle_client() o caminho da biblioteca.
ex: cx_Oracle.init_oracle_client(lib_dir=os.getcwd() + "\\app\\instantclient_19_9\\")

Após informe as credênciais de acesso ao banco de dados ou crie algum arquivo de login e passe as credências.
user='usuario_banco_dados', 
password='senha_banco_dados', 
dsn='localhost,1521,XE'

5º Passo
No arquivo controle.py informe o seu diretório de Download para a variável diretorio_download.


Outras bibliotecas que são necessárias para execução estão listadas no arquivo requirements.txt.
