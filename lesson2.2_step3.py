from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.ID, 'num1')
    x2 = browser.find_element(By.ID, 'num2')
    y = int(x1.text) + int(x2.text)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(y))
    browser.find_element(By. CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
    

