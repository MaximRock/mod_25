import pytest
from selenium import webdriver
import time


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('http://petfriends1.herokuapp.com/login')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('maxrockvardil@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    # time.sleep(10)

def test_all_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('maxrockvardil@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234567')
    # time.sleep(10)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    # names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    # descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    # time.sleep(10)
    print('Привет')

    for i in range(len(images)):
        assert images[i].get_attribute('src') != ''
        # assert names[i].text != ''
        # assert descriptions[i].text != ''
        # assert ', ' in descriptions[i]
        # parts = descriptions[i].text.split(", ")
        # assert len(parts[0]) > 0
        # assert len(parts[1]) > 0

        # time.sleep(10)
