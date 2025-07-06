import pytest
from pages.upload_download_page import UploadDownloadPage


@pytest.mark.parametrize("file_name", [
    "market-yandex.jpg",
    "sumup-unsplash.jpg"
])
def test_file_upload(driver, file_name):
    upload_download_page = UploadDownloadPage(driver)
    upload_download_page.open()
    upload_download_page.upload_file(file_name)
    assert upload_download_page.uploaded_file_path_contains(file_name), f"Файл {file_name} не был загружен"


def test_file_download(driver):
    upload_download_page = UploadDownloadPage(driver)
    upload_download_page.open()
    upload_download_page.click_download_button()
    assert upload_download_page.file_was_downloaded_successfully(), "Файл не был загружен"
