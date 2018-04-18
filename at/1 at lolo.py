from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.moscow.megafon.ru")
assert "Официальный сайт &laquo;МегаФон&raquo; Московский регион" in driver.title
