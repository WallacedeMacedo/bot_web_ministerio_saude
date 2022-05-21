# bot_web_ministerio_saude
Bot Ministério da Saúde.

Este Bot foi desenvolvido para baixar o arquivo compactado(rar, zip e 7z) no site do Ministério da Saúde. 

Após o download o arquivo é movido do diretório Download para o diretório arquivos/compactados dentro do projeto, em seguida os arquivos são extraidos no 
diretório arquivos/extraidos e carregados no banco de dados oracle.

Antes de executar o projeto é preciso seguir os passos abaixo.

Algumas bibliotecas são necessárias para execução e estão listadas no arquivo requirements.txt.

Edite o arquivo conexao_database.py e informe os dados de acesso ao banco de dados ou crie algum arquivo de login e passe as credências de acesso ao banco.

Após realizar o passo acima é preciso fazer o download do "Oracle Instant Client" de acordo com o seu sistema operacional, segue o link abaixo. 
https://www.oracle.com/br/database/technologies/instant-client/downloads.html

É importante passar o caminho/diretório do "Oracle Instant Client" em conexao_database.py e informe a tabela criada no banco de dados para ser carregada.
