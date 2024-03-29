from test_kazanexpress.pages.basket_page import basket_page_delete


def test_delete_from_basket():

    basket_page_delete.open()

    basket_page_delete.add_item_to_basket()
    basket_page_delete.delete_item_from_basket()

    basket_page_delete.should_basket_empty()
