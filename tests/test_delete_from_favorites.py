
from test_kazanexpress.pages.favorites_page import favorites_page_delete


def test_delete_from_favorites():

    favorites_page_delete.open()

    favorites_page_delete.add_item_to_favorites()
    favorites_page_delete.delete_item_from_favorites()

    favorites_page_delete.should_favorites_empty()
