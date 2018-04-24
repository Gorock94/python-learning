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
    driver.maximize_window()
def b2bBasket():
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a').click() #первый тариф на витрине
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/div[2]/a[2]').click() #добавление в корзину
#   z = driver.find_element_by_css_selector('body') #крутим вверх, чтобы был норм хедер #с этим разберемся позже
#   z.send_keys(Keys.HOME)
#   WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "b-b2b-cart-popup__goto")))
#   driver.find_element_by_class_name("b-b2b-cart-popup__goto").click() #клик по корзине
    driver.get("https://moscow.megafon.ru/corporate/cart/") #костылик
    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[4]/div/div[1]/form/ul/li[1]/a").click()
    entityField = driver.find_element_by_name("entity") #забиваем поля
    entityField.send_keys("test")
    innField = driver.find_element_by_name("inn")
    innField.send_keys("1234567894")
    fioField = driver.find_element_by_name("fio")
    fioField.send_keys("test")
    mailField = driver.find_element_by_name("mail")
    mailField.send_keys("vasily.balazhiy@dalee.ru")
    phoneField = driver.find_element_by_name("phone")
    phoneField.send_keys("9207035327")
    cityField = driver.find_element_by_name("city")
    cityField.send_keys("test")
    noteField = driver.find_element_by_name("note")
    noteField.send_keys("Эта заявка была отправлена в процессе автоматического тестирования сайта Мегафон. Вы можете закрывать её, не перезванивая и не уточняя") #v is for vezhlivost
    driver.find_element_by_class_name("b-b2b-cart-v2-order__button").click()
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "b-b2b-cart-v2-order__message_type_result")))
    driver.close()
    return print("PASS")
initialize(url)
b2bBasket()