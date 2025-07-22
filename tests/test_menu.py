import pytest
from pages.menu_page import MenuPage


@pytest.mark.parametrize("menu_item", ["MAIN_ITEM_1", "MAIN_ITEM_2", "MAIN_ITEM_3"])
def test_main_menu_items_visible(driver, menu_item):
    menu_page = MenuPage(driver)
    menu_page.open()
    assert menu_page.is_menu_visible(menu_item), f"{menu_item} не отображается"


def test_hover_sub_sub_items(driver):
    menu_page = MenuPage(driver)
    menu_page.open()
    menu_page.hover_over_element("MAIN_ITEM_2")
    menu_page.hover_over_element("SUB_SUB_LIST")
    assert menu_page.is_menu_visible("SUB_SUB_ITEM_1"), "Sub Sub Item 1 не отображается"
    assert menu_page.is_menu_visible("SUB_SUB_ITEM_2"), "Sub Sub Item 2 не отображается"
