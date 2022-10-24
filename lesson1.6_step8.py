from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"
i = 1

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    print(elements)
    for element in elements:
        element.send_keys(i)
        i += 1

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
