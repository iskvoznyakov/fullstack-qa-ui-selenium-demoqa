import pytest
from pages.tool_tips_page import ToolTipsPage


@pytest.mark.parametrize("element_name, expected_text", [
    ("button", "You hovered over the Button"),
    ("text_field", "You hovered over the text field"),
    ("contrary_word", "You hovered over the Contrary"),
    ("section_word", "You hovered over the 1.10.32")
])
def test_hover(driver, element_name, expected_text):
    tooltips_page = ToolTipsPage(driver)
    tooltips_page.open()
    tooltips_page.hover_over_element(element_name)
    text = tooltips_page.get_hover_text(element_name)
    assert text.strip() == expected_text, \
        f"Expected tooltip '{expected_text}' for {element_name}, but got '{text}'"
