import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path='drivers/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    dc = DesiredCapabilities.CHROME
    dc["goog:loggingPrefs"] = {"browser": "ALL"}

    browser = webdriver.Chrome(
                               options=options,
                               service=service,
                               desired_capabilities=dc
                               )

    browser.implicitly_wait(10)

    yield browser
    browser.quit()

