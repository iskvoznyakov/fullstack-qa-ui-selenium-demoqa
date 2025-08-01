from pages.dragabble_page import DragabblePage


def test_drag_simple_element(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("simple_tab")

    start_x, start_y = dragabble_page.get_simple_element_position()
    dragabble_page.drag_simple_element_by_offset(100, 50)
    end_x, end_y = dragabble_page.get_simple_element_position()

    assert (end_x, end_y) != (start_x, start_y), "Элемент на вкладке Simple не был перемещён"
