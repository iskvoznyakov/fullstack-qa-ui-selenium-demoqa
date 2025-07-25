import pytest
from pages.sortable_page import SortablePage


@pytest.mark.parametrize("from_index, to_index, expected_order", [
    (0, 5, ['Two', 'Three', 'Four', 'Five', 'Six', 'One']),
    (5, 0, ['Six', 'One', 'Two', 'Three', 'Four', 'Five'])
])
def test_sort_list_items(driver, from_index, to_index, expected_order):
    sortable_page = SortablePage(driver)
    sortable_page.open()
    sortable_page.drag_and_drop(from_index, to_index)
    actual_order = sortable_page.get_list_items()
    assert actual_order == expected_order, f"Ожидаемая сортировка {expected_order} не совпадает с фактической {actual_order}"
