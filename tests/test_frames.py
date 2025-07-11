import pytest
from pages.frames_page import FramesPage


@pytest.mark.parametrize("frame_name", [
    "frame_1",
    "frame_2"
])
def test_switch_to_frame(driver, frame_name):
    frames_page = FramesPage(driver)
    frames_page.open()
    text = frames_page.get_text_from_frame(frame_name)
    assert text == "This is a sample page", f"Неверный текст в {frame_name}: {text}"
