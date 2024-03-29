import allure
from selene import browser, have


class SearchPositive:

    @allure.step('Открываем браузер на странице https://kazanexpress.ru/')
    def open(self):
        browser.open('/')
        return self

    @allure.step('В поле поиска вводим поисковой запрос "Кастрюли"')
    def fill_search_field(self):
        browser.element('[data-test-id=input__search]').type('Кастрюли').press_enter()
        return self

    @allure.step('Проверяем результат поиска в тайтле поиска есть слово "Кастрюли и ковши"')
    def check_search_result(self):
        browser.element('[data-test-id=text__title]').should(have.text('Кастрюли и ковши'))


search_page = SearchPositive()
