import pytest
from pages.selectable_page import SelectablePage


@pytest.mark.parametrize("indexes", [
    [1],
    [2, 4]
])
def test_select_list_items(driver, indexes):
    selectable_page = SelectablePage(driver)
    selectable_page.open()
    selectable_page.switch_to_tab("List")
    selectable_page.select_elements("List", indexes)
    selected_elements = selectable_page.are_correct_elements_selected("List", indexes)
    assert selected_elements, f"Выбраны некорректные элементы во вкладке List - {selected_elements}, вместо {indexes}"


@pytest.mark.parametrize("indexes", [
    [1],
    [2, 4],
    [3, 7, 9]
])
def test_select_grid_items(driver, indexes):
    selectable_page = SelectablePage(driver)
    selectable_page.open()
    selectable_page.switch_to_tab("Grid")
    selectable_page.select_elements("Grid", indexes)
    selected_elements = selectable_page.are_correct_elements_selected("Grid", indexes)
    assert selected_elements, f"Выбраны некорректные элементы во вкладке Grid - {selected_elements}, вместо {indexes}"
