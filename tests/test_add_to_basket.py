from test_kazanexpress.pages.basket_page import basket_page


def test_add_to_basket():

    basket_page.open()
    basket_page.add_item_to_basket()
    basket_page.should_item_in_basket()
