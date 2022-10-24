from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return log(abs(12 * sin(x)))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, 'book').click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'solve').click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(3)
    browser.quit
