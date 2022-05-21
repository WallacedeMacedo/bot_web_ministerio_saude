import shutil  # move o arquivo entre diretórios
import os


class MoverArquivo:

    def __init__(self, arquivo, diretorio_origem, diretorio_destino):

        self.arquivo = arquivo
        self.diretorio_origem = diretorio_origem
        self.diretorio_destino = diretorio_destino

    # Passando o nome do arquivo e do diretório origem e destino.
    def mover(self):

        try:
            origem = os.path.join(self.diretorio_origem, self.arquivo)
            destino = os.path.join(self.diretorio_destino, self.arquivo)

            try:
                shutil.move(origem, destino)
                # shutil.move(self.diretorio_origem, self.diretorio_destino)
                return 1
            except ValueError as e:
                raise Exception('EEEE: {}'.format(e)) from None

        # except shutil.Error:
        except ValueError as e:
            raise Exception('AAAA: {}'.format(e)) from None
