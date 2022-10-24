from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
    return log(abs(12 * sin(x)))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    browser.execute_script('window.scrollBy(0, 100);')
    browser.find_element(By.ID, 'answer').send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox').click()
    option2 = browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()