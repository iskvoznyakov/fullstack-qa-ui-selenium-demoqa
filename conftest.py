import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    options.page_load_strategy = 'eager'

    download_dir = os.path.join(os.getcwd(), "tests", "for_tests", "downloads")
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
    os.makedirs(download_dir)

    prefs = {
        "download.default_directory": download_dir
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # Получаем результат выполнения теста
    outcome = yield
    rep = outcome.get_result()

    # Проверяем: если тест "упал" на этапе вызова
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Прикрепляем скриншот
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            # Прикрепляем HTML страницы
            allure.attach(
                driver.page_source,
                name="Page Source",
                attachment_type=allure.attachment_type.HTML
            )
