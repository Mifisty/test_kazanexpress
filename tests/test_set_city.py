from test_kazanexpress.pages.city_page import city_page


def test_set_city():

    city_page.open()
    city_page.set_city()
    city_page.should_city_changes()
