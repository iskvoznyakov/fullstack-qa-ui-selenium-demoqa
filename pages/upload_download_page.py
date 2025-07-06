import time
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from utils.decorators import log_action
import os


class UploadDownloadPage(BasePage):
    DOWNLOAD_BUTTON = (By.ID, "downloadButton")
    UPLOAD_BUTTON = (By.XPATH, "//input[@id='uploadFile']")
    UPLOAD_FILE_OUTPUT = (By.ID, "uploadedFilePath")

    def open(self):
        super().open(BASE_URL + "/upload-download")

    @log_action
    def upload_file(self, filename: str):
        elem = self.find(self.UPLOAD_BUTTON)
        elem.send_keys(os.path.join(os.getcwd(), "tests", "for_tests", "images", filename))

    @log_action
    def uploaded_file_path_contains(self, filename: str) -> bool:
        return filename in self.get_text(self.UPLOAD_FILE_OUTPUT)

    @log_action
    def click_download_button(self):
        self.click(self.DOWNLOAD_BUTTON)

    @log_action
    def file_was_downloaded_successfully(self, timeout=15):
        download_dir = os.path.join(os.getcwd(), "tests", "for_tests", "downloads")
        expected_filename = "sampleFile.jpeg"
        expected_path = os.path.join(download_dir, expected_filename)

        for _ in range(timeout * 2):
            if os.path.exists(expected_path):
                return True
            time.sleep(0.5)
        return False
