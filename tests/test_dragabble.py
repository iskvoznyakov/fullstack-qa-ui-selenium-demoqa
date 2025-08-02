from pages.dragabble_page import DragabblePage


def test_drag_simple_element(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("simple_tab")
    start_x, start_y = dragabble_page.get_element_position("drag_me_element")
    dragabble_page.drag_element_by_offset("drag_me_element", 100, 50)
    end_x, end_y = dragabble_page.get_element_position("drag_me_element")
    assert (end_x, end_y) != (start_x, start_y), "Элемент на вкладке Simple не был перемещён"


def test_drag_element_x_axis_only(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("axis_restricted_tab")
    start_x, start_y = dragabble_page.get_element_position("only_x_element")
    dragabble_page.drag_element_by_offset("only_x_element", 100, 50)
    end_x, end_y = dragabble_page.get_element_position("only_x_element")
    assert start_x != end_x, "Элемент 'Only X' на вкладке Axis Restricted не был перемещён по оси X"
    assert start_y == end_y, "Элемент 'Only X' на вкладке Axis Restricted был перемещён по оси Y"


def test_drag_element_y_axis_only(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("axis_restricted_tab")
    start_x, start_y = dragabble_page.get_element_position("only_y_element")
    dragabble_page.drag_element_by_offset("only_y_element", 100, 50)
    end_x, end_y = dragabble_page.get_element_position("only_y_element")
    assert start_y != end_y, "Элемент 'Only Y' на вкладке Axis Restricted не был перемещён по оси Y"
    assert start_x == end_x, "Элемент 'Only Y' на вкладке Axis Restricted был перемещён по оси X"
