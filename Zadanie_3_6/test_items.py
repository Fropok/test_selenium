import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    button_add_cart = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button_add_cart.is_displayed(), 'ОШИБКА! Кнопка добавления в корзину не найдена'


# Команда для запуска теста: pytest --language=es Zadanie_3_6/test_items.py
# Не хочется плодить репозитории, буду признателен за понимание!
