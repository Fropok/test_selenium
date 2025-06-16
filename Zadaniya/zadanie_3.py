import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/test_selenium/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    x_value = driver.find_element(By.ID, 'treasure')
    x_value = calc(x_value.get_attribute('valuex'))
    driver.find_element(By.ID, 'answer').send_keys(x_value)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
