import allure
from selene import browser, have


def test_search_positive():
    with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
        browser.open('/')

    with allure.step('В поле поиска вводим поисковой запрос "Кастрюли"'):
        browser.element('[data-test-id=input__search]').type('Кастрюли').press_enter()

    with allure.step('Проверяем результат поиска (в тайтле поиска есть слово "Кастрюли и ковши"'):
        browser.element('[data-test-id=text__title]').should(have.text('Кастрюли и ковши'))
