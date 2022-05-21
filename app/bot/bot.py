from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.common.exceptions import TimeoutException, WebDriverException
from datetime import datetime, timedelta
import os
import locale
import time


def esperar_download():

    data = (datetime.today() - timedelta(1)).strftime("%d%b%Y").lower()
    arquivo_rar = 'HIST_PAINEL_COVIDBR_{}.rar'.format(data)
    arquivo_zip = 'HIST_PAINEL_COVIDBR_{}.zip'.format(data)
    arquivo_7z = 'HIST_PAINEL_COVIDBR_{}.7z'.format(data)
    # caminho = '/home/wallace/Downloads'
    caminho = "C:\\Users\\Wallace\\Downloads\\"
    # print(os.path.join(caminho, arquivo))
    print('Aguarde o Download do arquivo.')

    while not os.path.exists(os.path.join(caminho, arquivo_rar) or
                             os.path.join(caminho, arquivo_zip) or os.path.join(caminho, arquivo_7z)):
        time.sleep(1)

    if os.path.isfile(os.path.join(caminho, arquivo)):
        print('Downlaod finalizado.')
        print('{0} localizado no diretório {1}.'.format(arquivo, caminho))
    else:
        print('{0} não localizado no diretório {1}.'.format(arquivo, caminho))


class Bot:

    @staticmethod
    def bot_web():

        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        # Extendendo o Driver do navegador Chrome, Firefox ou Edge.
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Chrome('C:\driver_chrome\chromedriver.exe')

        try:
            # Passando para a variável o link do site.
            url = 'https://covid.saude.gov.br/'

            # Abrindo o site.
            driver.get(url)
            download = '/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button'
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            wait.until(ec.visibility_of_element_located((By.XPATH, download)))
            # Passando o caminho do botão a ser clicado.
            driver.find_element(by=By.XPATH, value=download).click()

            esperar_download()
            # time.sleep(40)

        except TimeoutException as ex:
            print(ex)
        except WebDriverException as ex:
            print(ex)
        finally:
            # Fechando o navegador.
            driver.quit()

# class Bot:
#     bot_web()
