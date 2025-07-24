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


@pytest.mark.parametrize("color", [
    "Yellow",
    "Blue"
])
def test_select_value_from_old_style_select_menu(driver, color):
    select_menu_page = SelectMenuPage(driver)
    select_menu_page.open()
    selected = select_menu_page.select_value_from_old_style_select_menu(color)
    assert selected == color, f"Ожидалось {color}, а получено {selected}"


@pytest.mark.parametrize("values", [
    ["Green", "Black", "Blue", "Red"],
    ["Green", "Red"]
])
def test_select_value_from_multi_select_dropdown(driver, values):
    select_menu_page = SelectMenuPage(driver)
    select_menu_page.open()
    select_menu_page.select_values_from_multi_select_dropdown(values)
    selected_values = select_menu_page.get_selected_multi_values()
    assert set(values) == set(selected_values), f"{values} не совпадают с {selected_values}"


@pytest.mark.parametrize("values", [
    ["volvo", "opel"],
    ["saab", "audi"]
])
def test_select_value_from_standard_multi_select(driver, values):
    select_menu_page = SelectMenuPage(driver)
    select_menu_page.open()
    selected = select_menu_page.select_values_from_standard_multi_select(values)
    assert set([value.capitalize() for value in values]) == set(selected), f"{values} не выбран. Получено: {selected}"
