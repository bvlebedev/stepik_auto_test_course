from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return log(abs(12 * sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(2)
    browser.quit()

    
    
