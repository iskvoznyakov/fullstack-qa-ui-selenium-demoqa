import pytest

from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_the_login_form(username="test_user", password="Test@1234")
    assert login_page.is_login_successful(), "Авторизация не прошла"


@pytest.mark.parametrize("username, password", [
    ("", "Test@1234"),
    ("test_user", "")

])
def test_unsuccessful_login_without_required_fields(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_the_login_form(username=username, password=password)
    assert login_page.is_required_error_displayed(username=username,
                                                  password=password), "Ошибка об обязательности заполнения поля не отображается"


@pytest.mark.parametrize("username, password", [
    ("test_user_1", "Test@1234"),
    ("test_user", "Test@1234_1")

])
def test_unsuccessful_login_without_incorrect_fields(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.fill_the_login_form(username=username, password=password)
    assert login_page.is_invalid_error_displayed(), "Ошибка о некорректном заполнении полей не отображается"
