from test_kazanexpress.pages.login_page import LoginPage


def test_login_negative():
    login_page = LoginPage()

    login_page.open()

    login_page.click_login_button()
    login_page.fill_phone_number()

    login_page.should_error_message()




    # with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
    #     browser.open('/')
    # with allure.step('Кликаем на кнопку логина'):
    #     browser.element('[data-test-id=button__auth]').click()
    # with allure.step('Проверяем что открылся поп-ап авторизации'):
    #     browser.element('.sign-in-phone').should(have.text('Введите номер телефона'))
    # with allure.step('Вводим неверный номер телефона'):
    #     browser.element('.no-after').click().type('1').press_enter()
    # with allure.step('Проверяем, что выдало ошибку'):
    #     browser.element('.error-text').should(have.text('Неверный формат номера'))
    #

