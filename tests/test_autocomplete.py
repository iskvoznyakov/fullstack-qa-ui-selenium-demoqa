import pytest
from pages.autocomplete_page import AutocompletePage


@pytest.mark.parametrize("color", [
    "Red",
    "Green"
])
def test_enter_single_color(driver, color):
    autocomplete_page = AutocompletePage(driver)
    autocomplete_page.open()
    autocomplete_page.enter_single_color(color)
    selected_color = autocomplete_page.get_selected_single_color()
    assert selected_color == color, f"Выбран не {color}, а {selected_color}"


@pytest.mark.parametrize("colors", [
    ["Red", "Green"],
    ["Yellow", "Blue"]
])
def test_enter_multiple_colors(driver, colors):
    autocomplete_page = AutocompletePage(driver)
    autocomplete_page.open()
    autocomplete_page.enter_multiple_colors(colors)
    selected_colors = autocomplete_page.get_selected_multiple_colors()
    assert set(colors) == selected_colors, f"Выбраны не {colors}, а {selected_colors}"


def test_autocomplete_suggestions_start_with_input(driver):
    autocomplete_page = AutocompletePage(driver)
    autocomplete_page.open()
    autocomplete_page.input_single_color_partial("B")
    suggestions = autocomplete_page.get_dropdown_suggestions()
    assert suggestions, "Подсказки не появились при вводе 'B'"
    for suggestion in suggestions:
        assert suggestion.startswith("B"), f"Подсказка не начинается с 'B': {suggestion}"


def test_autocomplete_selects_from_suggestion(driver):
    autocomplete_page = AutocompletePage(driver)
    autocomplete_page.open()
    autocomplete_page.input_single_color_partial("B")
    suggestions = autocomplete_page.get_dropdown_suggestions()
    expected = suggestions[0]
    autocomplete_page.select_first_suggestion()
    selected = autocomplete_page.get_selected_single_color()
    assert selected == expected, f"Выбран не {expected}, а {selected}"
