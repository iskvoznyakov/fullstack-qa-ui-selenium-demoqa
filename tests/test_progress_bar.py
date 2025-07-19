import pytest
from pages.progress_bar_page import ProgressBarPage


@pytest.mark.parametrize("value", [30, 70])
def test_progress_bar_partial_stop(driver, value):
    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.open()
    progress_bar_page.start_progress()
    progress_bar_page.wait_for_progress_to_reach(value)
    current_value = int(progress_bar_page.get_progress_value())
    assert current_value >= value, f"Expected progress >= {value}%, but got {current_value}%"

def test_progress_bar_full_reset(driver):
    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.open()
    progress_bar_page.start_progress()
    progress_bar_page.wait_for_progress_to_reach(100, stop_after=False)
    progress_bar_page.reset_progress()
    current_value = int(progress_bar_page.get_progress_value())
    assert current_value == 0, f"Expected progress to be 0% after reset, but got {current_value}%"
