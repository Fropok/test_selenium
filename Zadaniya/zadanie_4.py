import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/test_selenium/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    numb_1 = driver.find_element(By.ID, 'num1')
    numb_2 = driver.find_element(By.ID, 'num2')
    sum_numbs = int(numb_1.text) + int(numb_2.text)
    Select(driver.find_element(By.ID, 'dropdown')).select_by_value(str(sum_numbs))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    driver.quit()
