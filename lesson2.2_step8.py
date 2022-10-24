from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('key1')
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('key2')
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('key2')
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    print(os.path.abspath(__file__))  # местоположение + имя файла
    print(os.path.abspath(os.path.dirname(__file__)))  # местоположение файла
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()
