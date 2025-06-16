import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

link = 'https://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/kyrspitona/SELENIUM/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    element_x = calc(driver.find_element(By.ID, 'input_value').text)
    driver.execute_script("window.scrollTo(0, 150);")
    driver.find_element(By.ID, 'answer').send_keys(element_x)
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()
