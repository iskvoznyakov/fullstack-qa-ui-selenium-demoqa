from pages.check_box_page import CheckBoxPage
import pytest


@pytest.mark.parametrize("checkbox_name", [
    "Notes", "React", "Public"
])
def test_select_one_checkbox(driver, checkbox_name):
    check_box_page = CheckBoxPage(driver)
    check_box_page.open()
    check_box_page.expand_all_the_checkboxes()
    check_box_page.click_checkbox_by_name(checkbox_name)
    assert check_box_page.is_checkbox_selected(checkbox_name), f"Чек-бокс {checkbox_name} не был выбран"


@pytest.mark.parametrize("parent_checkbox, child_checkboxes", [
    ("Desktop", ["Notes", "Commands"]),
    ("Office", ["Public", "Private", "Classified", "General"])
])
def test_select_multiple_checkboxes(driver, parent_checkbox, child_checkboxes):
    check_box_page = CheckBoxPage(driver)
    check_box_page.open()
    check_box_page.expand_all_the_checkboxes()
    check_box_page.click_checkbox_by_name(parent_checkbox)
    assert check_box_page.is_checkbox_selected(parent_checkbox), f"Чек-бокс {parent_checkbox} не был выбран"
    assert check_box_page.are_checkboxes_selected(child_checkboxes), f"Чек-боксы {child_checkboxes} не были выбраны"


@pytest.mark.parametrize("checkbox_name", [
    "Notes", "React", "Public"
])
def test_unselect_checkbox(driver, checkbox_name):
    check_box_page = CheckBoxPage(driver)
    check_box_page.open()
    check_box_page.expand_all_the_checkboxes()
    check_box_page.click_checkbox_by_name(checkbox_name)
    assert check_box_page.is_checkbox_selected(checkbox_name), f"Чек-бокс {checkbox_name} не был выбран"
    check_box_page.click_checkbox_by_name(checkbox_name)
    assert not check_box_page.is_checkbox_selected(checkbox_name), f"Чек-бокс {checkbox_name} по-прежнему выбран"
