import time

import pytest
from pages.select_menu_page import SelectMenuPage


@pytest.mark.parametrize("value", [
    "A root option",
"Group 1, option 1"
])
def test_select_value_from_select_value_dropdown(driver, value):
    select_menu_page = SelectMenuPage(driver)
    select_menu_page.open()
    select_menu_page.select_value_from_select_value_dropdown(value)
    selected_value = select_menu_page.get_selected_single_value()
    assert selected_value == value, f"Выбран не {value}, а {selected_value}"


@pytest.mark.parametrize("value", [
    "Dr.",
    "Prof."
])
def test_select_value_from_select_one_dropdown(driver, value):
    select_menu_page = SelectMenuPage(driver)
    select_menu_page.open()
    select_menu_page.select_value_from_select_one_dropdown(value)
    selected_value = select_menu_page.get_selected_single_value()
    assert selected_value == value, f"Выбран не {value}, а {selected_value}"
