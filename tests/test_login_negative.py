from test_kazanexpress.pages.login_page import login_page


def test_login_negative():

    login_page.open()

    login_page.click_login_button()
    login_page.fill_phone_number()

    login_page.should_error_message()
