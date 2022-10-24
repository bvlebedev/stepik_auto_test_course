from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

    