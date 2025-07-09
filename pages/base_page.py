from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self, url):
        logger.info(f"Переход на страницу: {url}")
        self.driver.get(url)

    def find(self, locator):
        logger.info(f"Поиск элемента: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator), f"There's no element: {locator}")

    def find_in_dom(self, locator):
        logger.info(f"Поиск элемента в DOM без ожидания видимости: {locator}")
        return self.driver.find_element(*locator)

    def click(self, locator):
        logger.info(f"Клик по элементу: {locator}")
        self.find(locator).click()

    def enter_text(self, locator, text):
        logger.info(f"Ввод '{text}' в: {locator}")
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator):
        logger.info(f"Проверка видимости {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        logger.info(f"Получение текста из {locator}")
        return self.find(locator).text

    def is_clickable(self, locator):
        logger.info(f"Проверка кликабельности {locator}")
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def switch_to_new_window(self):
        original = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != original:
                self.driver.switch_to.window(handle)
                return

    def get_alert(self):
        try:
            self.wait.until(EC.alert_is_present())
            return self.driver.switch_to.alert
        except (NoAlertPresentException, TimeoutException):
            return None

    def alert_text(self):
        alert = self.get_alert()
        if alert:
            return alert.text

    def alert_accept(self):
        alert = self.get_alert()
        if not alert:
            raise AssertionError("Ожидался alert, но он не появился")
        alert.accept()

    def alert_dismiss(self):
        alert = self.get_alert()
        if not alert:
            raise AssertionError("Ожидался alert, но он не появился")
        alert.dismiss()

    def alert_send_keys(self, text):
        alert = self.get_alert()
        if not alert:
            raise AssertionError("Ожидался alert, но он не появился")
        alert.send_keys(text)
        alert.accept()
