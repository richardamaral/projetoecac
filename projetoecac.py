import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pyautogui

import pandas as pd


url = "https://cav.receita.fazenda.gov.br/autenticacao/login"


chrome_options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-plugins")
options.add_argument("--disable-blink-features=BlockCredentialedSubresources")


user_agent = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"


navegador = webdriver.Chrome(options=chrome_options)



def iniciarnavegador():
    navegador.get(url)
    navegador.maximize_window()

def entrarecac():
    entrarecac = navegador.find_element(By.XPATH, '//*[@id="login-dados-certificado"]/p[2]/input')
    entrarecac.click()

def escolhercertificado():
    #pyautogui.click(1002,649,duration=1) #firefox options - seu certificado digital
    #pyautogui.click(942,598,duration=1) #firefox options - cert ok
    time.sleep(0.2)
    #pyautogui.click(942,598) #firefox options - cert ok
    pyautogui.click(1011, 683, duration=1) #chrome options - seu certificado digital
    pyautogui.click(847, 331, duration=1) #chrome options - certificado ok
    pyautogui.click(847,331,duration=0.8) #chrome options - certificado ok

def prepararconsulta():
    cnpj_data = []
    nome_data = []
    situacao_data = []
    datavigencia_data = []
    senhaseprocuracoes = navegador.find_element(By.XPATH, '//*[@id="btn302"]/a')
    senhaseprocuracoes.click()
    cadastroconsultascancelamento = navegador.find_element(By.XPATH, '//*[@id="containerServicos302"]/div/ul/li/a')
    time.sleep(0.4)
    cadastroconsultascancelamento.click()
    time.sleep(1.5)
    WebDriverWait(navegador, 30)
    frame = navegador.find_element(By.XPATH, '//*[@id="frmApp"]')
    navegador.switch_to.frame(frame)
    consultarprocurador = navegador.find_element(By.XPATH, '//*[@id="consultaProcurador"]')
    consultarprocurador.click()
    time.sleep(0.5)
    consultar = navegador.find_element(By.XPATH, '//*[@id="botProcurador"]')
    consultar.click()
    time.sleep(8.4)
    WebDriverWait(navegador,30)
    pularpravinte = navegador.find_element(By.XPATH, '//*[@id="proxBloc_21"]')
    pularpravinte.click()
    time.sleep(8.2)
    irproximasecao = navegador.find_element(By.XPATH, '//*[@id="proxBloc_41"]')
    irproximasecao.click()
    time.sleep(8.1)
    irproximasecao = navegador.find_element(By.XPATH, '//*[@id="proxBloc_61"]')
    irproximasecao.click()
    time.sleep(7.2)
    irproximasecao = navegador.find_element(By.XPATH, '//*[@id="proxBloc_81"]')
    irproximasecao.click()
    time.sleep(7.5)
    for i in range(2, 101):
        xpath = f'//*[@id="pag_{i}"]'
        for y in range(2, 21):
            cnpj = navegador.find_element(By.XPATH, f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[1]/font')
            cnpj = cnpj.text
            cnpj = cnpj.strip()



            nomeoutorgante = navegador.find_element(By.XPATH, f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[2]/font')
            nomeoutorgante = nomeoutorgante.text
            nomeoutorgante = nomeoutorgante.strip()
            nome = nomeoutorgante

            try:
                cancelada = navegador.find_element(By.XPATH,f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[5]/div[1]/label')
                if cancelada.is_displayed():
                    cancelada = cancelada.text
                    cancelada = cancelada.strip()
                    situacao_text = cancelada

                else:
                    situacao = navegador.find_element(By.XPATH,f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[5]/font')
                    situacao = situacao.text
                    situacao = situacao.strip()
                    situacao_text = situacao
            except:
                situacao = navegador.find_element(By.XPATH, f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[5]/font')
                situacao = situacao.text
                situacao = situacao.strip()
                situacao_text = situacao


            datavigencia1 = navegador.find_element(By.XPATH,f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[3]/font')
            datavigencia2 = navegador.find_element(By.XPATH,f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[3]/font/br[1]')
            datavigencia3 = navegador.find_element(By.XPATH,f'/html/body/div/div[2]/form/table[2]/tbody/tr[{y}]/td[3]/font/br[2]')

            datavigencia = datavigencia1, datavigencia2, datavigencia3



            datavigencia1_text = datavigencia[0].text.strip()
            datavigencia2_text = datavigencia[1].text.strip()
            datavigencia3_text = datavigencia[2].text.strip()

            datavigencia_text = f'{datavigencia1_text} {datavigencia2_text} {datavigencia3_text}'
            datavigencia_text = datavigencia_text.replace('\n', ' ')

            cnpj_data.append(cnpj)
            nome_data.append(nome)
            situacao_data.append(situacao_text)
            datavigencia_data.append(datavigencia_text)

            print("CNPJ:", cnpj)
            print("Nome:", nome)
            print("Situação:", situacao_text)
            print("Data de Vigência:", datavigencia_text)
            print("-------------------------------------")

        proxima_pagina = None

        try:
            proxima_pagina = navegador.find_element(By.XPATH, xpath)
            proxima_pagina.click()
        except:
            print("não encontrei o xpath")# Se não encontrou o elemento, continua para o próximo XPath

        if proxima_pagina is None:
            print("Nenhum botão de próxima página encontrado")
        time.sleep(5)
        print("Pagina", i, "ACIMA")
        continue



    data = {
        'CNPJ': cnpj_data,
        'Nome': nome_data,
        'Situação': situacao_data,
        'Data de Vigência': datavigencia_data
    }

    print("Comprimento de cnpj_data:", len(cnpj_data))
    print("Comprimento de nome_data:", len(nome_data))
    print("Comprimento de situacao_data:", len(situacao_data))
    print("Comprimento de datavigencia_data:", len(datavigencia_data))
    input("APERTE [ENTER] PARA CRIAR A PLANILHA")
    df = pd.DataFrame(data)
    df.to_excel('dados.xlsx', index=False)



    time.sleep(1000)




iniciarnavegador()
time.sleep(1.5)
entrarecac()
WebDriverWait(navegador, 30)
time.sleep(3)
escolhercertificado()
WebDriverWait(navegador, 30)
time.sleep(2.5)
prepararconsulta()




