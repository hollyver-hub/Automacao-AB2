from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("http://www.dominiopublico.gov.br/")
time.sleep(2)

element = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/select")
element.click()
time.sleep(2)
element = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/select/option[4]")
element.click()
time.sleep(2)
element = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[7]/td[3]/table/tbody/tr/td[1]/a/img")
element.click()
time.sleep(2)

dados_documentos = []

while True:
    for linhas in range(1, 51):
        try:
            time.sleep(2)
            documentos = driver.find_element(By.XPATH, f"/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[{linhas}]/td[3]/a")
            documentos.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(6)

            titulo = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[1]/td[3]").text
            genero = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[3]/a").text
            autor = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[3]/td[3]").text
            instituicao_parceira = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[5]/td[3]/a").text
            instituicao_programa = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[6]/td[3]").text
            area_conhecimento = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[7]/td[3]").text
            nivel_documento = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[8]/td[3]").text
            ano_tese = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[9]/td[3]").text
            resumo = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[11]/td[3]").text

            dados_documentos.append({
                'Título': titulo,
                'Gênero': genero,
                'Autor': autor,
                'Instituição Parceira': instituicao_parceira,
                'Instituição Programa': instituicao_programa,
                'Área do Conhecimento': area_conhecimento,
                'Nível do Documento': nivel_documento,
                'Ano da Tese': ano_tese,
                'Resumo': resumo
            })
            print(dados_documentos)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"Não foi possível processar o documento na linha {linhas}: {e}")
            continue

    time.sleep(2)
    try:
        element = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > center:nth-child(1) > span:nth-child(2) > a:nth-child(10)")
        element.click()
    except:
        break
    time.sleep(2)

df = pd.DataFrame(dados_documentos)
df.to_csv('documentos.csv', index=False, encoding='utf-8')

driver.quit()
