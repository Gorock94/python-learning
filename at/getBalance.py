from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
url = 'https://lk.megafon.ru/login/'
DicNumber = {}
DicNumber['9260019435'] = 'СтФ:'
DicNumber['9260018617'] = 'СтФ:'
DicNumber['9310010048'] = 'Спб:'
DicNumber['9310010023'] = 'Спб:'
DicNumber['9300560305'] = 'НН:'
DicNumber['9300560254'] = 'НН:'
DicNumber['9383153580'] = 'КФ:'
DicNumber['9382946494'] = 'КФ:'
DicNumber['9231012389'] = 'СФ:'
DicNumber['9321180456'] = 'УФ:'
DicNumber['9321180463'] = 'УФ:'
DicNumber['9397001073'] = 'ПФ:'
DicNumber['9397000683'] = 'ПФ:'
DicNumber['9241001548'] = 'ДВФ:'
DicNumber['9241001510'] = 'ДВФ:'
#class CheckMoney():
def initialize(url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
def getMoney(num):
    moneyAndNumber = {}
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.NAME, "j_username")))
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.NAME, "j_password")))
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-button-but")))
    numberField = driver.find_element_by_name("j_username")
    passwordField = driver.find_element_by_name("j_password")
    numberField.send_keys(Keys.CONTROL + 'a')
    numberField.send_keys(Keys.BACKSPACE)
    numberField.send_keys(num)
    passwordField.send_keys(Keys.CONTROL + 'a')
    passwordField.send_keys(Keys.BACKSPACE)
    passwordField.send_keys('test12')
    driver.find_element_by_class_name("ui-button-but").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gadget_account")))
    w =  driver.find_element_by_css_selector('h1').text
    if w != "Вход":
        money = driver.find_element_by_css_selector('[class="gadget_account"]').find_element_by_css_selector('div h3').text
        l = []
    else:
        money = "error"
        l = []
    for i in money:
        if i != ' ':
            l.append(i)
    money = ''.join(l)
    driver.close()
    return money
for num in DicNumber.keys():
    initialize(url)
    money = getMoney(num)
    print('{0} {1} {2}'.format(DicNumber[num], num, money))