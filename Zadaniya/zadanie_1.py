from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    service = Service('/Users/maksimkuznetsov/PycharmProjects/kyrspitona/SELENIUM/drivers/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(link)
    driver.maximize_window()

    input1 = driver.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.XPATH, '//input[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
