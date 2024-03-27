import allure
from selene import browser, have


def test_login_button():
    with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
        browser.open('/')
    with allure.step('Кликаем на кнопку логина'):
        browser.element('[data-test-id=button__auth]').click()
    with allure.step('Проверяем что открылся поп-ап авторизации'):
        browser.element('.sign-in-phone').should(have.text('Введите номер телефона'))

