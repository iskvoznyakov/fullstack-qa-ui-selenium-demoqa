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


def test_drag_within_box_container(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("container_restricted_tab")
    dragabble_page.drag_element_by_offset("within_box_element", 300, 300)
    box = dragabble_page.get_element_rect("within_box_element")
    container = dragabble_page.get_container_rect("wrapper_box")
    assert box["x"] >= container["x"], "Левая граница элемента вышла за пределы контейнера"
    assert box["y"] >= container["y"], "Верхняя граница элемента вышла за пределы контейнера"
    assert box["x"] + box["width"] <= container["x"] + container["width"], \
        "Правая граница элемента вышла за пределы контейнера"
    assert box["y"] + box["height"] <= container["y"] + container["height"], \
        "Нижняя граница элемента вышла за пределы контейнера"


def test_drag_within_parent_container(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("container_restricted_tab")
    dragabble_page.drag_element_by_offset("within_parent_element", 50, 50)
    box = dragabble_page.get_element_rect("within_parent_element")
    container = dragabble_page.get_container_rect("parent_box")
    assert box["x"] >= container["x"], "Левая граница элемента (parent) вышла за пределы родительского контейнера"
    assert box["y"] >= container["y"], "Верхняя граница элемента (parent) вышла за пределы родительского контейнера"
    assert box["x"] + box["width"] <= container["x"] + container["width"], \
        "Правая граница элемента (parent) вышла за пределы родительского контейнера"
    assert box["y"] + box["height"] <= container["y"] + container["height"], \
        "Нижняя граница элемента (parent) вышла за пределы родительского контейнера"


def test_drag_elements_with_cursor_styles(driver):
    dragabble_page = DragabblePage(driver)
    dragabble_page.open()
    dragabble_page.click_on_tab("cursor_style_tab")
    for element in ["center_cursor", "top_left_cursor", "bottom_cursor"]:
        start = dragabble_page.get_element_position(element)
        dragabble_page.drag_element_by_offset(element, 50, 50)
        end = dragabble_page.get_element_position(element)

        assert end != start, f"Элемент {element} не был перемещён на вкладке Cursor Style"
