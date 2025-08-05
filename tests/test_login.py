from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.fill_the_login_form(username="test_user", password="Test@1234")

    assert login_page.is_login_successful(), "Авторизация не прошла"
