from selenium import webdriver
from pynput.mouse import Button, Controller
from time import sleep
import time
import pandas
import random

#Abro la pagina

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://es.tradingview.com/symbols/AUDUSD/technicals/')

#Maximizo

mouse = Controller()

mouse.position = (985, 17)
mouse.click(Button.left, 1)

sleep(1)


#Abro tabla con indicadores a 1 minuto

data_frame1m = pandas.read_csv("Tabla1m.csv")

#Abro tabla con indicadores a 5 minutos

data_frame5m = pandas.read_csv("Tabla5m.csv")

#EMPIEZO LA CAPTURA DE DATOS

contador = 0

while contador < 480:

    contador += 1

    #Datos a 1 minuto
    mouse = Controller()

    mouse.position = (1358, 633)
    mouse.click(Button.left, 1)

    sleep(1)

    mouse.position = (248, 311)
    mouse.click(Button.left, 1)

    sleep(random.randint(6,10))

    # EXTRAER LOS DATOS

    # GENERAL

    precio = float(driver.find_element_by_xpath('.//div[@class="tv-symbol-price-quote__value js-symbol-last"]').text)
    volumen = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[3]/div[3]/div[1]').text
    volumen = volumen.replace('K', '')
    volumen = float(volumen)

    # OSILADORES

    RSI = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
    RSI = RSI.replace('−', '-')
    RSI = float(RSI)
    Estocastico = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
    Estocastico = Estocastico.replace('−', '-')
    Estocastico = float(Estocastico)
    ICPB = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
    ICPB = ICPB.replace('−', '-')
    ICPB = float(ICPB)
    IMDM = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]').text
    IMDM = IMDM.replace('−', '-')
    IMDM = float(IMDM)
    OA = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
    OA = OA.replace('−', '-')
    OA = float(OA)
    Momento = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[2]').text
    Momento = Momento.replace('−', '-')
    Momento = float(Momento)
    MACD = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
    MACD = MACD.replace('−', '-')
    MACD = float(MACD)
    RSIR = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
    RSIR = RSIR.replace('−', '-')
    RSIR = float(RSIR)
    Williams = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[10]/td[2]').text
    Williams = Williams.replace('−', '-')
    Williams = float(Williams)
    BBP = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[11]/td[2]').text
    BBP = BBP.replace('−', '-')
    BBP = float(BBP)
    OU = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[12]/td[2]').text
    OU = OU.replace('−', '-')
    OU = float(OU)

    # MOMENTOS

    MME5 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text)
    MMS5 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[3]/td[2]').text)
    MME10 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[4]/td[2]').text)
    MMS10 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[2]').text)
    # MME20 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[6]/td[2]').text
    # MMS20 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]').text
    # MME30 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[8]/td[2]').text
    # MMS30 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[9]/td[2]').text
    MME50 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[10]/td[2]').text)
    MMS50 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[11]/td[2]').text)
    # MME100 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[12]/td[2]').text
    # MMS100 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[13]/td[2]').text
    # MME200 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[14]/td[2]').text
    # MMS200 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[15]/td[2]').text
    # nube = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[16]/td[2]').text
    # MMPV = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[17]/td[2]').text
    # hull = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[18]/td[2]').text


    #Fijo la Hora

    hora = time.strftime("%H.%M.%S")
    # GUARDAR LOS DATOS

    Datos1m = {'1': precio, '2': volumen, '3': ['-'], '4': ['-'], '5': ['-'], '6': ['-'], '7': RSI, '8': Estocastico,
               '9': ICPB, '10': IMDM, '11': OA, '12': Momento, '13': MACD, '14': RSIR, '15': Williams, '16': BBP,
               '17': OU, '18': hora, '19': MME5, '20': MMS5, '21' : MME10, '22' : MMS10, '23' : MME50, '24' : MMS50}
    data_frame1m = data_frame1m.append(Datos1m, ignore_index=True)


    #DATOS A 5 MINUTOS

    mouse = Controller()

    mouse.position = (331, 309)
    mouse.click(Button.left, 1)

    sleep(random.randint(6,10))

    # GENERAL

    precio = float(driver.find_element_by_xpath('.//div[@class="tv-symbol-price-quote__value js-symbol-last"]').text)
    volumen = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[3]/div[3]/div[1]').text
    volumen = volumen.replace('K', '')
    volumen = float(volumen)

    # OSILADORES

    RSI = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
    RSI = RSI.replace('−','-')
    RSI = float(RSI)
    Estocastico = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
    Estocastico = Estocastico.replace('−', '-')
    Estocastico = float(Estocastico)
    ICPB = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
    ICPB = ICPB.replace('−', '-')
    ICPB = float(ICPB)
    IMDM = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]').text
    IMDM = IMDM.replace('−', '-')
    IMDM = float(IMDM)
    OA = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
    OA = OA.replace('−', '-')
    OA = float(OA)
    Momento = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[7]/td[2]').text
    Momento = Momento.replace('−', '-')
    Momento = float(Momento)
    MACD = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
    MACD = MACD.replace('−', '-')
    MACD = float(MACD)
    RSIR = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
    #RSIR = RSIR.replace('−', '-')
    RSIR = float(RSIR)
    Williams = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[10]/td[2]').text
    Williams = Williams.replace('−', '-')
    Williams = float(Williams)
    BBP = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[11]/td[2]').text
    BBP = BBP.replace('−', '-')
    BBP = float(BBP)
    OU = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[12]/td[2]').text
    OU = OU.replace('−', '-')
    OU = float(OU)

    # MOMENTOS

    MME5 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text)
    MMS5 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[3]/td[2]').text)
    MME10 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[4]/td[2]').text)
    MMS10 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[2]').text)
    # MME20 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[6]/td[2]').text
    # MMS20 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]').text
    # MME30 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[8]/td[2]').text
    # MMS30 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[9]/td[2]').text
    MME50 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[10]/td[2]').text)
    MMS50 = float(driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[11]/td[2]').text)
    # MME100 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[12]/td[2]').text
    # MMS100 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[13]/td[2]').text
    # MME200 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[14]/td[2]').text
    # MMS200 = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[15]/td[2]').text
    # nube = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[16]/td[2]').text
    # MMPV = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[17]/td[2]').text
    # hull = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[18]/td[2]').text

    # GUARDAR LOS DATOS

    Datos1m = {'1': precio, '2': volumen, '3': ['-'], '4': ['-'], '5': ['-'], '6': ['-'], '7': RSI, '8': Estocastico,
               '9': ICPB, '10': IMDM, '11': OA, '12': Momento, '13': MACD, '14': RSIR, '15': Williams, '16': BBP,
               '17': OU, '18': hora, '19': MME5, '20': MMS5, '21' : MME10, '22' : MMS10, '23' : MME50, '24' : MMS50}
    data_frame5m = data_frame5m.append(Datos1m, ignore_index=True)

    #ACTUALIZO LA PAGINA

    driver.refresh()

    #guardo la captura de los datos

    data_frame5m.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\Capturadedatos\Tabla5m.csv', index=False, header=True)
    data_frame1m.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\Capturadedatos\Tabla1m.csv', index=False, header=True)


    sleep(random.randint(6,10))
print(data_frame1m)
#Termino la captura de datos
