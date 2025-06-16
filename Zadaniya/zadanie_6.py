import math

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/test_selenium/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys('Maksim')
    driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys('Kuz')
    driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('mmm@mail.ru')
    # получаем элемент файла (кнопка добавить файл)
    element_file = driver.find_element(By.ID, 'file')
    # получаем путь до файла (где он хранится)
    file_path = Path(__file__).parent /'files'/'file.txt'
    # загружаем файл
    element_file.send_keys(str(file_path))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()
