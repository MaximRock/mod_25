import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\Driver/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # pytest.driver.set_window_size(1200, 1200)

    yield

    pytest.driver.quit()

def test_my_pets_page():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('maxrockvardil@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # нажимаем кнопку с тремя черточками
    pytest.driver.find_element_by_xpath('//span[@class="navbar-toggler-icon"]').click()
    # time.sleep(5)
    # нажимаем кнопку мои питомцы
    pytest.driver.find_element_by_xpath('//a[text()="Мои питомцы"]').click()
    # time.sleep(5)

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h2")))

    # мой логин вносим в переменную
    # my_login = element.text
    # time.sleep(5)
    # проверяем что мы находимся на странице мои питомцы
    assert pytest.driver.find_element_by_tag_name('h2').text == element.text


def test_number_of_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('maxrockvardil@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # нажимаем кнопку с тремя черточками
    pytest.driver.find_element_by_xpath('//span[@class="navbar-toggler-icon"]').click()
    # time.sleep(5)
    # нажимаем кнопку мои питомцы
    pytest.driver.find_element_by_xpath('//a[text()="Мои питомцы"]').click()


    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, ".\\.col-sm-4 left")))
    # time.sleep(5)
    # statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")
    # time.sleep(5)
    number = element[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    rows = pytest.driver.find_element_by_css_selector('table.table-hover')
    assert number == len(rows)





