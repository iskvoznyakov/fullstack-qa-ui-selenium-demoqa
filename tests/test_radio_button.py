from pages.radio_button_page import RadioButtonPage
import pytest


@pytest.mark.parametrize("radio_button_name", [
    "Yes", "Impressive"
])
def test_select_clickable_radio_button(driver, radio_button_name):
    radio_button_page = RadioButtonPage(driver)
    radio_button_page.open()
    radio_button_page.select_radio_button_by_name(radio_button_name)
    selected_result = radio_button_page.get_selected_result()
    assert selected_result == radio_button_name, f"Выбран не {radio_button_name}, а {selected_result}"


def test_check_disabled_radio_button(driver):
    radio_button_page = RadioButtonPage(driver)
    radio_button_page.open()
    assert radio_button_page.is_radio_button_disabled("No"), "Radiobutton 'No' активен"
