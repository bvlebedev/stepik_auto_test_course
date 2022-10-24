from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_find = browser.find_element(By.ID, "treasure")  # нашли картинку
    x_element = x_find.get_attribute("valuex")  # получили значение атрибута картинки
    print(x_element)
    y = calc(x_element)  # рассчитали выражение
    answer = browser.find_element(By.ID, "answer")  # ищем поле для написания ответа
    answer.send_keys(y)  # заполняем поле данными "y"
    option1 = browser.find_element(By.ID, "robotCheckbox")  # ищем чекбокс и проставляем 
    option1.click()  # кликаем по нему
    option2 = browser.find_element(By.ID, "robotsRule")  #  находим радиобаттон
    option2.click()  # устанавлиаем значок на "роботы рулят"
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


