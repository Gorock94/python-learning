from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
url = 'https://moscow.megafon.ru/corporate/mobile/tariffs/alltariffs/'
#class b2bBasket():
def initialize(url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
def b2bBasket():
    driver.find_element_by_class_name("b-tariff-item__link").click()
    WebDriverWait(driver, 2000)
    z = driver.find_element_by_css_selector('body')
    z.send_keys(Keys.END)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/a[2]').click()
    WebDriverWait(driver, 4000).until(EC.presence_of_element_located((By.CLASS_NAME, "b-b2b-cart-popup__goto")))
    driver.find_element_by_class_name("b-b2b-cart-popup__goto").click()
    WebDriverWait(driver, 4000).until(EC.presence_of_element_located((By.CLASS_NAME, "b-b2b-cart-v2__title")))
    driver.find_element_by_class_name("b-b2b-cart-v2-order__contract b-b2b-cart-v2-order__contract_type_paper ").click()
    entityField = driver.find_element_by_name("entity")
    innField = driver.find_element_by_name("inn")
    fioField = driver.find_element_by_name("fio")
    mailField = driver.find_element_by_name("mail")
    phoneField = driver.find_element_by_name("phone")
    cityField = driver.find_element_by_name("city")
    noteField = driver.find_element_by_name("note")
    entityField.send_keys("test")
    innField.send_keys("1234567894")
    fioField.send_keys("test")
    mailField.send_keys("vasily.balazhiy@dalee.ru")
    phoneField.send_keys("9207035327")
    cityField.send_keys("test")
    noteField.send_keys("Эта заявка была отправлена в процессе автоматического тестирования сайта Мегафон. Вы можете закрывать её, не перезванивая и не уточняя")
    driver.find_element_by_class_name("b-b2b-cart-v2-order__button").click()
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "b-b2b-cart-v2-order__message_type_result")))
    driver.close()
    return print("PASS")
initialize(url)
b2bBasket()