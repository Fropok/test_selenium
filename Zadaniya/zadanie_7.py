import math

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/test_selenium/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.switch_to.alert.accept()
    # time.sleep(1)
    x = driver.find_element(By.ID, 'input_value').text
    driver.find_element(By.ID, 'answer').send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print(driver.switch_to.alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    driver.quit()
