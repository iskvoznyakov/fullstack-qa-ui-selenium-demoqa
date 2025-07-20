import pytest
from pages.tabs_page import TabsPage


@pytest.mark.parametrize("tab_name, expected_text", [
    ("what_tab", "Lorem Ipsum is simply dummy text of the printing and typesetting industry."),
    ("origin_tab", "Contrary to popular belief, Lorem Ipsum is not simply random text."),
    ("use_tab",
     "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.")])
def test_tabs_content(driver, tab_name, expected_text):
    tabs_page = TabsPage(driver)
    tabs_page.open()
    tabs_page.click_tab(tab_name)
    text = tabs_page.get_tab_content(tab_name)
    assert expected_text in text.strip(), f"Expected content for {tab_name}: {expected_text}, but got empty text"


def test_default_tab_is_active(driver):
    tabs_page = TabsPage(driver)
    tabs_page.open()
    assert tabs_page.is_tab_active("what_tab"), "Expected 'what_tab' to be active by default"
    for tab in ["origin_tab", "use_tab"]:
        assert not tabs_page.is_tab_active(tab), f"Expected {tab} to be inactive"


@pytest.mark.parametrize("first_tab, second_tab", [
    ("what_tab", "origin_tab"),
    ("origin_tab", "use_tab"),
    ("use_tab", "what_tab")
])
def test_switch_tabs(driver, first_tab, second_tab):
    tabs_page = TabsPage(driver)
    tabs_page.open()
    tabs_page.click_tab(first_tab)
    tabs_page.click_tab(second_tab)
    assert tabs_page.is_tab_active(second_tab), f"Expected {second_tab} to be active"
    assert not tabs_page.is_tab_active(first_tab), f"Expected {first_tab} to be inactive"
