import os
import datetime
from app.funcoes.data import Data
from app.funcoes.arquivo_compactado import BuscarArquivo
from app.funcoes.mover_arquivos import MoverArquivo
from app.funcoes.extrair_arquivo import ExtrairArquivo
from app.funcoes.arquivo_csv import ArquivoCsv
from app.funcoes.estrutura_sql import EstruturaSql
from app.funcoes.conexao_database import ConexaoOracle
from app.bot.bot import Bot


diretorio_download = "C:\\Users\\Wallace\\Downloads\\"
diretorio_compactados = os.getcwd() + "\\app\\arquivos\\compactados\\"
diretorio_extraidos = os.getcwd() + "\\app\\arquivos\\extraidos\\"

data = Data()


class Controle:

    def comportamento(nome_arquivo):
        extrair_arquivo = ExtrairArquivo(nome_arquivo, diretorio_compactados, diretorio_extraidos)
        extrair_arquivo.extrair()
        procurar_csv = ArquivoCsv(diretorio_extraidos, data.data_ano(), data.data_ontem(), data.data_hoje())
        nova_lista = procurar_csv.buscar_csv()  # retorna lista

        if nova_lista != 0:
            tratamento = EstruturaSql(nova_lista)
            estrutura_montada = tratamento.montar_sql()  # retorna lista
            db_oracle = ConexaoOracle(estrutura_montada)
            db_oracle.truncate_table()
            db_oracle.inserir_dados()
            # print('BD Carregado.')
            print('Fim do processo: ', datetime.datetime.today())

    while True:
        print('Início do processo: ', datetime.datetime.today())

        # Procurando arquivo_compactado no diretório Downloads
        procurar_compactado = BuscarArquivo(diretorio_download, data.data_hoje(), data.data_ontem())
        nome_arquivo = procurar_compactado.buscar()
        # print(nome_Arquivo)

        if nome_arquivo != 0:
            mover_arquivo = MoverArquivo(nome_arquivo, diretorio_download, diretorio_compactados)
            mover_arquivo.mover()
            comportamento(nome_arquivo)
            break
        else:
            # Procurando arquivo_compactado no diretório "\\app\\arquivos\\compactados\\"
            procurar_compactado = BuscarArquivo(diretorio_compactados, data.data_hoje(), data.data_ontem())
            nome_arquivo = procurar_compactado.buscar()

            if nome_arquivo != 0:
                comportamento(nome_arquivo)
                break
            else:
                bot = Bot
                bot.bot_web()
