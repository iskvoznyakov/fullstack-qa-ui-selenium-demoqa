from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def test_successful_logout(driver):
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    login_page.open()
    login_page.fill_the_login_form(username="test_user", password="Test@1234")
    assert login_page.is_login_successful(), "Авторизация не прошла"

    profile_page.logout()
    assert profile_page.is_logout_successful(), "Выхода из профиля не произошло"
