import pytest
from pages.sortable_page import SortablePage


@pytest.mark.parametrize("from_index, to_index, expected_order", [
    (0, 5, ['Two', 'Three', 'Four', 'Five', 'Six', 'One']),
    (5, 0, ['Six', 'One', 'Two', 'Three', 'Four', 'Five'])
])
def test_sort_list_items(driver, from_index, to_index, expected_order):
    sortable_page = SortablePage(driver)
    sortable_page.open()
    sortable_page.switch_to_tab("List")
    sortable_page.drag_and_drop("List", from_index, to_index)
    actual_order = sortable_page.get_items("List")
    assert actual_order == expected_order, f"Ожидаемая сортировка {expected_order} не совпадает с фактической {actual_order}"


@pytest.mark.parametrize("from_index, to_index, expected_order", [
    (0, 5, ['Two', 'Three', 'Four', 'Five', 'Six', 'One', 'Seven', 'Eight', 'Nine']),
    (5, 0, ['Six', 'One', 'Two', 'Three', 'Four', 'Five', 'Seven', 'Eight', 'Nine'])
])
def test_sort_grid_items(driver, from_index, to_index, expected_order):
    sortable_page = SortablePage(driver)
    sortable_page.open()
    sortable_page.switch_to_tab("Grid")
    sortable_page.drag_and_drop("Grid", from_index, to_index)
    actual_order = sortable_page.get_items("Grid")
    assert actual_order == expected_order, f"Ожидаемая сортировка {expected_order} не совпадает с фактической {actual_order}"
