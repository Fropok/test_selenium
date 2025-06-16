import math

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/test_selenium/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'book'))).click()
    x = driver.find_element(By.ID, 'input_value').text
    driver.find_element(By.ID, 'answer').send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print(driver.switch_to.alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    driver.quit()
