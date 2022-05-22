from datetime import datetime, timedelta
import locale


class Data:
    # locale.getlocale()  # obtendo local atual.
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def __init__(self):
        self.dt_hoje = datetime.today()

    def data_ontem(self):
        # Formato da Data. Ex: 20nov2021
        ontem = self.dt_hoje - timedelta(2)
        dt_ontem = ontem.strftime("%d%b%Y").lower()
        return dt_ontem

    def data_hoje(self):
        # Formato da Data. Ex: 20nov2021
        dt_hoje = self.dt_hoje.strftime("%d%b%Y").lower()
        return dt_hoje

    def data_ano(self):
        ano_atual = self.dt_hoje.strftime("%Y").lower()
        return ano_atual
