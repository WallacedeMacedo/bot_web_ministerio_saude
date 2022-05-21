import os, datetime
from .funcoes.data import Data
from .funcoes.arquivo_compactado import BuscarArquivo
from .funcoes.mover_arquivos import MoverArquivo
from .funcoes.extrair_arquivo import ExtrairArquivo
from .funcoes.arquivo_csv import ArquivoCsv
from .funcoes.estrutura_sql import EstruturaSql
from .funcoes.conexao_database import ConexaoOracle
from .bot.bot import Bot


diretorio_download = "C:\\Users\\Wallace\\Downloads\\"
diretorio_compactados = os.getcwd()+ "\\app\\arquivos\\compactados\\"
diretorio_extraidos = os.getcwd()+ "\\app\\arquivos\\extraidos\\"


#diretorio_download = "/home/wallace/Downloads/"
#diretorio_compactados = os.getcwd() + "/app/arquivos/compactados/"
#diretorio_extraidos = os.getcwd() + "/app/arquivos/extraidos/"
data = Data()


class Controle:
    def comportamento(nome_Arquivo):
        extrair_Arquivo = ExtrairArquivo(nome_Arquivo, diretorio_compactados, diretorio_extraidos)
        extrair_Arquivo.extrair()
        procurar_Csv = ArquivoCsv(diretorio_extraidos, data.data_ano(), data.data_ontem(), data.data_hoje())
        nova_Lista = procurar_Csv.buscar_csv()  # retorna lista

        if (nova_Lista != 0):
            tratamento = EstruturaSql(nova_Lista)
            estrutura_montada = tratamento.montar_sql()  # retorna lista
            dbOracle = ConexaoOracle(estrutura_montada)
            dbOracle.truncate_table()
            dbOracle.inserir_dados()
            #print('BD Carregado.')
            print('Fim do processo: ', datetime.datetime.today())

    while True:
        print('Início do processo: ', datetime.datetime.today())

        # Procurando arquivo_compactado no diretório Downloads
        procurar_Compactado = BuscarArquivo(diretorio_download, data.data_hoje(), data.data_ontem())
        nome_Arquivo = procurar_Compactado.buscar()
        # print(nome_Arquivo)
        if (nome_Arquivo != 0):
            mover_Arquivo = MoverArquivo(nome_Arquivo, diretorio_download, diretorio_compactados)
            mover_Arquivo.mover()
            comportamento(nome_Arquivo)
            break
        else:
            # Procurando arquivo_compactado no diretório "\\app\\arquivos\\compactados\\"
            procurar_Compactado = BuscarArquivo(diretorio_compactados, data.data_hoje(), data.data_ontem())
            nome_Arquivo = procurar_Compactado.buscar()

            if (nome_Arquivo != 0):
                comportamento(nome_Arquivo)
                break
            else:
                bot = Bot
                bot.bot_web()
