import pytest
from pages.nested_frames_page import NestedFramesPage


@pytest.mark.parametrize("frame_name, expected_text", [
    ("parent_frame", "Parent frame"),
    ("child_frame", "Child Iframe"),
])
def test_check_text_in_frame(driver, frame_name, expected_text):
    nested_frames_page = NestedFramesPage(driver)
    nested_frames_page.open()

    if frame_name == "parent_frame":
        nested_frames_page.switch_to_parent_frame()
    else:
        nested_frames_page.switch_to_child_frame()

    text = nested_frames_page.get_text_from_body()
    assert text == expected_text, f"Неверный текст в {frame_name}: {text}"
