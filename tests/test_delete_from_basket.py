from test_kazanexpress.pages.basket_page import DeleteFromBasket


def test_delete_from_basket():
    basket_page = DeleteFromBasket()

    basket_page.open()

    basket_page.add_item_to_basket()
    basket_page.delete_item_from_basket()

    basket_page.should_basket_empty()










    # with allure.step('Открываем браузер на странице https://kazanexpress.ru/'):
    #     browser.open('/')
    #
    # with allure.step('В поле поиска вводим поисковой запрос "Кастрюли"'):
    #     browser.element('[data-test-id=input__search]').type('Кастрюля из нержавеющей стали').press_enter()
    # with allure.step('Кликаем на товар'):
    #     browser.all('[data-test-id=item__product-card]').element_by(have.text('Кастрюля из нержавеющей стали со стеклянной крышкой')).click()
    # with allure.step('Добавляем товар в корзину'):
    #     browser.all('[data-test-id=item__sku]').element_by(have.text('2 литра')).click()
    #     browser.element('[data-test-id=button__add-cart]').click()
    # with allure.step('Переходим в корзину'):
    #     browser.element('[data-test-id=button__cart]').click()
    # with allure.step('Удаляем товар из корзины'):
    #     browser.element('[data-test-id=button__delete-from-cart]').click()
    #
    # with allure.step('Проверяем то что в корзине нет товаров'):
    #     browser.element('[data-test-id=text__empty-favorite-title]').should(have.text('В корзине пока нет товаров'))
