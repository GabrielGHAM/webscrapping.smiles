import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option(
         'excludeSwitches', ['enable-logging'])
options.add_argument('--lang=pr-BR')
options.add_argument('--disable-notifications')
# options.add_argument(" --headless")
# options.add_argument('window-size=400,800')

voo_origem = input( 'Digite a origem \n')
voo_destino = input( 'Digite o destino\n')
voo_dia = input( 'Qual o dia?\n')
voo_mes = input( 'Qual o mês?\n')
qtd_adultos = int(input("Quantos adultos? "))
qtd_criancas = int(input("Quantas crianças? "))
qtd_bebes = int(input("Quantos bebês? "))
voo_mes = int(voo_mes) - 1
voo_mes = str(voo_mes)

# voo_ano = input( 'Qual ano\n')

navegador = webdriver.Chrome(options=options)
# navegador.set_window_position(-1000, 0)
navegador.maximize_window()
navegador.get('https://www.smiles.com.br/passagens')
sleep(2)
origem = navegador.find_element(By.ID, 'inputOrigin')

origem.send_keys(voo_origem)

sleep(1.5)

origem.send_keys(Keys.TAB)

sleep(0.5)

destino = navegador.find_element(By.ID, 'inputDestination')
destino.send_keys(voo_destino)

sleep(0.5)

destino.send_keys(Keys.TAB)

sleep(0.5)

selecIdaVolta = navegador.find_element(
    By.XPATH, '//*[@id="tripTypeSelectPosition1"]/div/div')
selecIdaVolta.click()

sleep(0.5)

Ida = navegador.find_element(
    By.XPATH, '//*[@id="tripTypeSelectPosition1"]/div/div/div/ul/li[2]')
Ida.click()

sleep(0.5)

calendario = navegador.find_element(
    By.NAME, '_smilesflightsearchportlet_WAR_smilesbookingportlet_departure_date')
calendario.click()

sleep(0.5)


while True:
    # Encontre os elementos para o mês atual e próximo mês
    meses = navegador.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//tbody//td[@class!=' ui-datepicker-unselectable ui-state-disabled ']")
    # Verifique se o mês desejado está sendo exibido
    if any(mes.get_attribute("data-month") == voo_mes and mes.get_attribute("data-year") == "2023" for mes in meses):
        break
    # Se o mês desejado não estiver sendo exibido, clique na seta para o próximo mês
    seta_proximo_mes = navegador.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/div/a')
    seta_proximo_mes.click()

for data in meses:
    if data.get_attribute("data-month") == voo_mes and data.get_attribute("data-year") == "2023" and data.find_element(By.XPATH, "./a").text == voo_dia:
        data.click()
        break

sleep(0.5)

confirmarBttn = navegador.find_element(
    By.XPATH, '//*[@id="ui-datepicker-div"]/div[4]/button[1]')
confirmarBttn.click()

sleep(1)


# adiciona os adultos
for i in range(qtd_adultos - 1):
    adicionarAdultos = navegador.find_element(By.CSS_SELECTOR, "button.more[data-for='qtyAdults']")
    adicionarAdultos.click()
    sleep(1.0)

# adiciona as crianças
for i in range(qtd_criancas):
    adicionarCrianças = navegador.find_element(By.CSS_SELECTOR, "button.more[data-for='qtyKids']")
    adicionarCrianças.click()
    sleep(1.0)

# adiciona os bebês
for i in range(qtd_bebes):
    adicionarBebes = navegador.find_element(By.CSS_SELECTOR, "button.more[data-for='qtyBabies']")
    adicionarBebes.click()
    sleep(1.0)


submitBttn = navegador.find_element(By.CLASS_NAME, 'btn-search-flight')
submitBttn.click()

wait = WebDriverWait(navegador, 20)

wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="select-flight-accordion-ida"]/div[2]/div/div[5]/div[1]/div[1]/div[1]')))


page_source = navegador.page_source


site = BeautifulSoup(page_source, 'html.parser')

infoVoo = site.find('div', {'class': 'select-flight-list-accordion-item'})

infoVoo_preco_milhas = site.find_all(
    'label', attrs={'class': 'flight-fare-input-container-control-label'})
infoVoo_preco_milhas = infoVoo_preco_milhas[2].text

infoVoo_companhia = infoVoo.find('span', {'class': 'company'})

infoVoo_companhia = infoVoo_companhia.text

infoVoo_info = site.find('div', {'class': 'info'}).find_all('p')

infoVoo_info = [info.text for info in infoVoo_info]

infoVoo_saida = infoVoo_info[1]
infoVoo_chegada = infoVoo_info[2]
infoVoo_cidade_inicio = infoVoo_info[3]
infoVoo_cidade_destino = infoVoo_info[4]

print('Companhia', infoVoo_companhia)
print('Saindo de', infoVoo_cidade_inicio)
print('Destino para', infoVoo_chegada)
print('Horário de saída', infoVoo_saida)
print('Horário de chegada', infoVoo_chegada)
print('Preço por milhas', infoVoo_preco_milhas)


# infoVoo_iata = infoVoo.find('p', {'class': 'iata-code'})


# print(infoVoo_companhia)

# navegador.quit()
# botão para diminuir adultos

# sleep(2)

# origem = site.find_elements(By.ID, 'inputOrigin')
# print(origem)

# sleep(2)

# origem.send_keys(Keys.ARROW_DOWN)
# origem.send_keys(Keys.RETURN)

# destino = site.find_element(By.ID, 'input-destination')
# destino.send_keys('Rio de Janeiro')

# sleep(2)

# destino.send_keys(Keys.ARROW_DOWN)
# destino.send_keys(Keys.RETURN)

# sleep(2)

# ida = site.find_element(By.ID, 'input-date-1')
# ida.send_keys('30/04/2022')

# sleep(2)

# volta = site.find_element(By.ID, 'input-date-2')
# volta.send_keys('05/05/2022')

# sleep(2)

# search_button = site.find_element(By.ID, 'flight-search-submit')
# search_button.click()

# # Exemplo: coletando o preço da primeira passagem encontrada
# price = site.find_element(By.CSS_SELECTOR, '.search-result-price .price-value')
# print(price.text)
