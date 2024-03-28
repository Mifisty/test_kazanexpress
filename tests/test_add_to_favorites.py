from test_kazanexpress.pages.favorites_page import AddToFavorites


def test_add_favorites():
    favorites_page = AddToFavorites()

    favorites_page.open()
    favorites_page.add_item_to_favorites()
    favorites_page.should_item_in_favorites()








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
    # with allure.step('Проверяем то что в избранном находится товар добавленный нами'):
    #     browser.element('[data-test-id=item__product-card]').should(have.text('Кастрюля из нержавеющей стали'))
