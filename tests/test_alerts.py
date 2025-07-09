import pytest

from pages.alerts_page import AlertsPage


def test_alert_shows_text_after_click(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_alert_button()
    assert alerts_page.alert_is_opened(), "Алерт не отображается"


def test_delayed_alert_shows_text_after_click(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_time_alert_button()
    assert alerts_page.delayed_alert_is_opened(), "Алерт с задержкой не отображается"


@pytest.mark.parametrize("action", [
    "accept",
    "dismiss"
])
def test_open_confirm_alert(driver, action):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_confirm_box_button()
    assert alerts_page.confirm_alert_is_opened(action), "Алерт с подтверждением не отображается"


@pytest.mark.parametrize("name", [
    "Ivan",
    "John"
])
def test_open_prompt_alert(driver, name):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_prompt_box_button()
    assert alerts_page.prompt_alert_is_opened(name), "Алерт с вводом текста не отображается"
