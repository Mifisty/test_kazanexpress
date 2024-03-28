
from test_kazanexpress.pages.favorites_page import DeleteFromFavorites


def test_delete_from_favorites():
    favorites_page = DeleteFromFavorites()

    favorites_page.open()

    favorites_page.add_item_to_favorites()
    favorites_page.delete_item_from_favorites()

    favorites_page.should_favorites_empty()







    # with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
    #     browser.open('/')
    # with allure.step('В поле поиска вводим поисковой запрос "Кастрюля из нержавеющей стали"'):
    #     browser.element('[data-test-id=input__search]').type('Кастрюля из нержавеющей стали').press_enter()
    # with allure.step('Кликаем на товар'):
    #     browser.all('[data-test-id=item__product-card]').element_by(have.text('Кастрюля из нержавеющей стали со стеклянной крышкой')).click()
    # with allure.step('Добавляем товар в избранное'):
    #     browser.all('[data-test-id=item__sku]').element_by(have.text('2 литра')).click()
    #     browser.all('[data-test-id=button__add-to-favorites]').element_by(have.text('В желания')).click()
    # with allure.step('Переходим в избранное'):
    #     browser.element('[data-test-id=button__wishes]').click()
    # with allure.step('Удаляем товар из избранного'):
    #     browser.element('[data-test-id=button__add-to-favorites]').click()
    # with allure.step('Проверяем то что в избранном нет товаров'):
    #     browser.element('[data-test-id=text__empty-favorite-title]').should(have.text('Добавьте то, что понравилось'))
