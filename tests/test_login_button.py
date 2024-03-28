import allure
from selene import browser, have

from test_kazanexpress.pages.login_page import LoginPage


def test_login_button():
    login_page = LoginPage

    login_page.open()
    login_page.click_login_button()
    login_page.should_pop_up_visible()





    # with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
    #     browser.open('/')
    #
    # with allure.step('Кликаем на кнопку логина'):
    #     browser.element('[data-test-id=button__auth]').click()
    #
    # with allure.step('Проверяем что открылся поп-ап авторизации'):
    #     browser.element('.sign-in-phone').should(have.text('Введите номер телефона'))

