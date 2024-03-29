from test_kazanexpress.pages.favorites_page import favorites_page


def test_add_favorites():

    favorites_page.open()
    favorites_page.add_item_to_favorites()
    favorites_page.should_item_in_favorites()
