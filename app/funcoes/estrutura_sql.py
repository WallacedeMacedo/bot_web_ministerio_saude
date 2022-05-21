class EstruturaSql:

    def __init__(self, lista_de_dados):
        self._regiao = None
        self._estado = None
        self._municipio = None
        self._coduf = None
        self._codmun = None
        self._codregiaosaude = None
        self._nomeregiaosaude = None
        self._data = None
        self._semanaepi = None
        self._populacaotcu2019 = None
        self._casosacumulado = None
        self._casosnovos = None
        self._obitosacumulado = None
        self._obitosnovos = None
        self._recuperadosnovos = None
        self._emacompanhamentonovos = None
        self._interiormetropolitana = None
        self.lista_Dados_Covid = lista_de_dados
        print('Montando estrutura SQL.')

    def montar_sql(self):
        dados_tratados = []

        for valor in self.lista_Dados_Covid:
            self.regiao = str(valor[0])
            self.estado = str(valor[1])
            self.municipio = str(valor[2])
            self.coduf = str(valor[3])
            self.codmun = str(valor[4])
            self.codregiaosaude = str(valor[5])
            self.nomeregiaosaude = str(valor[6])
            self.data = str(valor[7])
            self.semanaepi = str(valor[8])
            self.populacaotcu2019 = str(valor[9])
            self.casosacumulado = str(valor[10])
            self.casosnovos = str(valor[11])
            self.obitosacumulado = str(valor[12])
            self.obitosnovos = str(valor[13])
            self.recuperadosnovos = str(valor[14])
            self.emacompanhamentonovos = str(valor[15])
            self.interiormetropolitana = str(valor[16])

            sql = 'insert into dev.ext_covid_py(regiao, estado, municipio, coduf, codmun, codregiaosaude, nomeregiaosaude, data, semanaepi, populacaotcu2019, casosacumulado, casosnovos, obitosacumulado, obitosnovos, recuperadosnovos, emacompanhamentonovos, interiormetropolitana) values ('
            dados = '\'' + self.regiao + '\',' + '\'' + self.estado + '\',' + '\'' + self.municipio + '\',' + '\'' + self.coduf + '\',' + '\'' + self.codmun + '\',' + '\'' + self.codregiaosaude + '\',' + '\'' + self.nomeregiaosaude + '\',' + '\'' + self.data + '\',' + '\'' + self.semanaepi + '\',' + '\'' + self.populacaotcu2019 + '\',' + '\'' + self.casosacumulado + '\',' + '\'' + self.casosnovos + '\',' + '\'' + self.obitosacumulado + '\',' + '\'' + self.obitosnovos + '\',' + '\'' + self.recuperadosnovos + '\',' + '\'' + self.emacompanhamentonovos + '\',' + '\'' + self.interiormetropolitana + '\')'
            dados_tratados.append(sql + dados)

        return dados_tratados

    # Getter
    @property
    def regiao(self):
        return self._regiao

    # Setter
    @regiao.setter
    def regiao(self, valor):
        valor = valor.replace('nan', '')
        self._regiao = valor

    # Getter
    @property
    def estado(self):
        return self._estado

    # Setter
    @estado.setter
    def estado(self, valor):
        valor = valor.replace('nan', '')
        self._estado = valor

    # Getter
    @property
    def municipio(self):
        return self._municipio

    # Setter
    @municipio.setter
    def municipio(self, valor):
        valor = str(valor).replace('nan', '').replace("'", "\''")
        self._municipio = str(valor)

    # Getter
    @property
    def coduf(self):
        return self._coduf

    # Setter
    @coduf.setter
    def coduf(self, valor):
        valor = valor.replace('nan', '')
        self._coduf = valor

    # Getter
    @property
    def codmun(self):
        return self._codmun

    # Setter
    @codmun.setter
    def codmun(self, valor):
        valor = valor.replace('nan', '')
        self._codmun = valor

    # Getter
    @property
    def codregiaosaude(self):
        return self._codregiaosaude

    # Setter
    @codregiaosaude.setter
    def codregiaosaude(self, valor):
        valor = valor.replace('nan', '')
        self._codregiaosaude = valor

    # Getter
    @property
    def nomeregiaosaude(self):
        return self._nomeregiaosaude

    # Setter
    @nomeregiaosaude.setter
    def nomeregiaosaude(self, valor):
        valor = valor.replace('nan', '')
        self._nomeregiaosaude = valor

    # Getter
    @property
    def data(self):
        return self._data

    # Setter
    @data.setter
    def data(self, valor):
        valor = valor.replace('nan', '')
        self._data = valor

    # Getter
    @property
    def semanaepi(self):
        return self._semanaepi

    # Setter
    @semanaepi.setter
    def semanaepi(self, valor):
        valor = valor.replace('nan', '')
        self._semanaepi = valor

    # Getter
    @property
    def populacaotcu2019(self):
        return self._populacaotcu2019

    # Setter
    @populacaotcu2019.setter
    def populacaotcu2019(self, valor):
        valor = valor.replace('nan', '')
        self._populacaotcu2019 = valor

    # Getter
    @property
    def casosacumulado(self):
        return self._casosacumulado

    # Setter
    @casosacumulado.setter
    def casosacumulado(self, valor):
        valor = valor.replace('nan', '')
        self._casosacumulado = valor

    # Getter
    @property
    def casosnovos(self):
        return self._casosnovos

    # Setter
    @casosnovos.setter
    def casosnovos(self, valor):
        valor = valor.replace('nan', '')
        self._casosnovos = valor

    # Getter
    @property
    def obitosacumulado(self):
        return self._obitosacumulado

    # Setter
    @obitosacumulado.setter
    def obitosacumulado(self, valor):
        valor = valor.replace('nan', '')
        self._obitosacumulado = valor

    # Getter
    @property
    def obitosnovos(self):
        return self._obitosnovos

    # Setter
    @obitosnovos.setter
    def obitosnovos(self, valor):
        valor = valor.replace('nan', '')
        self._obitosnovos = valor

    # Getter
    @property
    def recuperadosnovos(self):
        return self._recuperadosnovos

    # Setter
    @recuperadosnovos.setter
    def recuperadosnovos(self, valor):
        valor = valor.replace('nan', '')
        self._recuperadosnovos = valor

    # Getter
    @property
    def emacompanhamentonovos(self):
        return self._emacompanhamentonovos

    # Setter
    @emacompanhamentonovos.setter
    def emacompanhamentonovos(self, valor):
        valor = valor.replace('nan', '')
        self._emacompanhamentonovos = valor

    # Getter
    @property
    def interiormetropolitana(self):
        return self._interiormetropolitana

    # Setter
    @interiormetropolitana.setter
    def interiormetropolitana(self, valor):
        valor = valor.replace('nan', '')
        self._interiormetropolitana = valor
