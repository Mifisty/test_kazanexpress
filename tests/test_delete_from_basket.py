from test_kazanexpress.pages.basket_page import basket_page


def test_delete_from_basket():

    basket_page.open()

    basket_page.add_item_to_basket()
    basket_page.delete_item_from_basket()

    basket_page.should_basket_empty()
