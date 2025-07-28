import pytest
from pages.resizable_page import ResizablePage


@pytest.mark.parametrize("x_offset, y_offset", [
    [-50, -50],
    [300, 100]
])
def test_resize_box_with_restriction(driver, x_offset, y_offset):
    resizable_page = ResizablePage(driver)
    resizable_page.open()
    initial_height, initial_width = resizable_page.get_box_size("box_with_restriction")
    resizable_page.resize_box_by_offset("box_with_restriction", x_offset, y_offset)
    current_height, current_width = resizable_page.get_box_size("box_with_restriction")
    assert initial_height + y_offset == current_height, f"Текущая высота {current_height} != {initial_height + y_offset}"
    assert initial_width + x_offset == current_width, f"Текущая ширина {current_width} != {initial_width + x_offset}"


@pytest.mark.parametrize("x_offset, y_offset", [
    [100, 200],
    [200, 300]
])
def test_resize_box_without_restriction(driver, x_offset, y_offset):
    resizable_page = ResizablePage(driver)
    resizable_page.open()
    initial_height, initial_width = resizable_page.get_box_size("box_without_restriction")
    resizable_page.resize_box_by_offset("box_without_restriction", x_offset, y_offset)
    current_height, current_width = resizable_page.get_box_size("box_without_restriction")
    assert initial_height + y_offset == current_height, f"Текущая высота {current_height} != {initial_height + y_offset}"
    assert initial_width + x_offset == current_width, f"Текущая ширина {current_width} != {initial_width + x_offset}"
