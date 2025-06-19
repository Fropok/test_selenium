import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from files.testdata import Testdata

# список проверяемых страниц
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


def func_number():
    '''Функция для ввода правильного ответа'''
    answer = math.log(int(time.time()))
    return answer


@pytest.mark.parametrize('link', links)
def test_stepik(browser, link):
    browser.get(link)

    # жмем "Войти"
    button_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//nav//a[text()="Войти"]')))
    button_login.click()

    # вводим логин
    input_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'id_login_email')))
    input_login.send_keys(Testdata.get_login())

    # вводим пароль
    input_password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'id_login_password')))
    input_password.send_keys(Testdata.get_password())

    # логинимся
    button_login = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    button_login.click()

    # проверка того, что залогинились
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Profile"]')))

    # вводим ответ
    input_answer = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.attempt textarea')))
    input_answer.send_keys(func_number())

    # отправляем ответ
    send_answer = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
    send_answer.click()

    # получаем текст ответа
    status_answer = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]')))
    status_answer = status_answer.text


    assertion_error = None

    try:
        assert status_answer == 'Correct!'
    except AssertionError as e:
        print(f'Ожидали получить: Correct!, получили: {status_answer}')
        assertion_error = e
    finally:
        # обнуляем задание
        button_decide_again = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="again-btn white"]')))
        button_decide_again.click()

    if assertion_error:
        raise assertion_error
