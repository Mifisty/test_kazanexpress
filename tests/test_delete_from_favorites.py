
from test_kazanexpress.pages.favorites_page import favorites_page


def test_delete_from_favorites():

    favorites_page.open()

    favorites_page.add_item_to_favorites()
    favorites_page.delete_item_from_favorites()

    favorites_page.should_favorites_empty()
