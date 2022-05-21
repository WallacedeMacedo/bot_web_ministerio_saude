import patoolib  # descompacta arquivos rar e zip
import py7zr  # descompacta arquivos 7z
import time  # pausa para aguardar a passagem do arquivo
from patoolib.util import PatoolError


class ExtrairArquivo:
    def __init__(self, arquivo_compactado, diretorio_rar, diretorio_excel):
        self.arquivo_Compactado = str(arquivo_compactado)
        self.diretorio_Origem_Rar = diretorio_rar
        self.diretorio_Destino_Excel = diretorio_excel

    def extrair(self):

        try:
            if self.arquivo_Compactado.endswith('.rar') or self.arquivo_Compactado.endswith('.zip'):

                # Extraindo arquivo.
                print("Extraindo...")
                # print(self.arquivo_Compactado)
                # print(self.diretorio_Destino_Excel)
                patoolib.extract_archive(self.diretorio_Origem_Rar + self.arquivo_Compactado,
                                         outdir=self.diretorio_Destino_Excel)
                time.sleep(2)
                return 1
            elif self.arquivo_Compactado.endswith('.7z'):
                # Extraindo arquivo.
                print("Extraindo...")
                archive = py7zr.SevenZipFile(self.arquivo_Compactado, mode='r', )
                archive.extractall(self.diretorio_Destino_Excel)
                archive.close()
                time.sleep(2)
                return 1
            else:
                print('Formato não suportado')
        except PatoolError as exc:
            print(exc)
            return 0
