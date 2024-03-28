import allure
from selene import browser, have


def test_set_city():
    with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
        browser.open('/')

    with allure.step('Кликаем на текущий город"'):
        browser.element('[data-test-id=button__select-city]').click()
    with allure.step('Выбираем город "Воронеж"'):
        browser.all('[data-test-id=list__city]').element_by(have.text('Воронеж')).click()

    with allure.step('Проверяем, что город поменялся на Воронеж'):
        browser.element('[data-test-id=button__select-city]').should(have.text('Воронеж'))
