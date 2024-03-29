from test_kazanexpress.pages.login_page import login_page


def test_login_button():

    login_page.open()
    login_page.click_login_button()
    login_page.should_pop_up_visible()
