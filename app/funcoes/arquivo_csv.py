import csv
import os
import pandas as pd
from pandas.core.frame import DataFrame


class ArquivoCsv:

    def __init__(self, diretorio_excel, data_ano_atual, data_ontem, data_hoje):
        self.diretorio_Excel = diretorio_excel
        self.data_Ano_Atual = data_ano_atual
        self.data_ontem = data_ontem
        self.data_hoje = data_hoje

    def buscar_csv(self):
        lista_arquivos_csv = []
        df = DataFrame()
        data_formatada = '_{}_'.format(self.data_Ano_Atual)
        # data_formatada = '_2021_'

        # Buscando arquivos CSV com o ano informado.
        print("Buscando arquivo em: " + self.diretorio_Excel)
        for diretorio, subpastas, arquivos in os.walk(self.diretorio_Excel):

            for arquivo in arquivos:
                if data_formatada in arquivo:
                    if self.data_ontem in arquivo:
                        # if self.data_hoje in arquivo:
                        # Buscar qualquer arquivo com a descrição passada na variável "data_formatada". ex: _2020_
                        print("Arquivo {} encontrado. ".format(arquivo))
                        lista_arquivos_csv.append(arquivo)

        # Unindo os arquivos encontrados acima.
        for arquivos_Csv in lista_arquivos_csv:
            diretorio_mais_arquivo = os.path.join(self.diretorio_Excel, arquivos_Csv)

            arquivo = pd.read_csv(diretorio_mais_arquivo, delimiter=';', quoting=csv.QUOTE_NONE)
            df = pd.concat([df, arquivo], axis=0, ignore_index=True, )

        # Renomeando o cabeçalho das colunas
        df = df.rename(columns={'regiao': 'regiao', 'estado': 'estado', 'municipio': 'municipio', 'coduf': 'coduf',
                                'codmun': 'codmun', 'codRegiaoSaude': 'codregiaosaude',
                                'nomeRegiaoSaude': 'nomeregiaosaude', 'data': 'data', 'semanaEpi': 'semanaepi',
                                'populacaoTCU2019': 'populacaoTCU2019', 'casosAcumulado': 'casosacumulado',
                                'casosNovos': 'casosnovos', 'obitosAcumulado': 'obitosacumulado',
                                'obitosNovos': 'obitosnovos', 'Recuperadosnovos': 'recuperadosnovos',
                                'emAcompanhamentoNovos': 'emacompanhamentonovos',
                                'interior/metropolitana': 'interiormetropolitana'})

        nova_lista = list(df.itertuples(index=False, name=None))
        return nova_lista
