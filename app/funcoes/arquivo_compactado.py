import os


class BuscarArquivo:

    def __init__(self, diretorio, dt_hoje, dt_ontem):
        # Passando os nomes do arquivo e do diretório.
        self.diretorio_Arquivo = diretorio
        self.data_Hoje = dt_hoje
        self.data_Ontem = dt_ontem

    def buscar(self):
        # Devido a alteração do nome do arquivo pelo MS, houve a necessidade de alterar o modo de busca do arquivo.
        print("Buscando arquivo em: " + self.diretorio_Arquivo)
        for diretorio, subpastas, arquivos in os.walk(self.diretorio_Arquivo):

            for arquivo in arquivos:
                if self.data_Ontem in arquivo:
                    # if self.data_Hoje in arquivo:
                    # Buscar qualquer arquivo no diretório Download que tenha na descrição o formato de data 23nov2021.
                    print("Arquivo {} encontrado. ".format(arquivo))
                    return arquivo

                # elif self.data_Ontem in arquivo:
                #     print("Arquivo {} encontrado. ".format(arquivo))
                #     return arquivo

        print('Arquivo não encontrado.')
        return 0
