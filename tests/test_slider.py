import pytest
from pages.slider_page import SliderPage


@pytest.mark.parametrize("value", [
    0,
    1,
    50,
    99,
    100
])
def test_set_slider(driver, value):
    slider_page = SliderPage(driver)
    slider_page.open()
    slider_page.set_slider_value(value)
    expected_value = slider_page.get_value()
    assert expected_value == str(value), f"Значение слайдера {value} не равно ожидаемому {expected_value}"
