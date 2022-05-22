import cx_Oracle
import os
from datetime import datetime

cx_Oracle.init_oracle_client(lib_dir=os.getcwd() + "\\app\\instantclient_19_9\\")
# cx_Oracle.init_oracle_client(lib_dir=r"D:\oraclexe\instantclient_19_9")
# É preciso informar o caminho do "Oracle Instant Client" na sua máquina.


class ConexaoOracle:

    def __init__(self, sql_insert):
        self.sql_insert = sql_insert

    @staticmethod
    def truncate_table():
        sql = 'truncate table dev.ext_covid_py'
        try:
            driver_conexao = cx_Oracle.connect(user='usuario_banco_dados', password='senha_banco_dados', dsn='localhost,1521,XE')
            cursor = driver_conexao.cursor()
            cursor.execute(sql)
            driver_conexao.commit()
            cursor.close()
            driver_conexao.close()
        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            print("Oracle-Error-Message:", error.message)

    def inserir_dados(self):
        try:
            print('Início do carregamento na base de dados: ', datetime.today())
            driver_conexao = cx_Oracle.connect(user='usuario_banco_dados', password='senha_banco_dados', dsn='localhost,1521,XE')
            cursor = driver_conexao.cursor()
            
            for sql in self.sql_insert:
                # print(sql)
                cursor.execute(sql)

            driver_conexao.commit()
            cursor.close()
            driver_conexao.close()
            print('Fim do Carregamento: ', datetime.today())

        except cx_Oracle.NotSupportedError as exc:
            error, = exc.args
            # print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)

        except cx_Oracle.DataError as exc:
            error, = exc.args
            # print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)

        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            # print("Oracle-Error-Code:", error.code)
            print("Oracle-Error-Message:", error.message)
