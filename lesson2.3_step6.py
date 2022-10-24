from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'trollface.btn').click()
   # new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By. CSS_SELECTOR, '.btn.btn-primary').click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(4)
    browser.quit()