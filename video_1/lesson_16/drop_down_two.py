import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.select import Select

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get('https://the-internet.herokuapp.com/dropdown')

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

all_options = DROPDOWN.options

for option in all_options:
    time.sleep(2)
    DROPDOWN.select_by_visible_text(option.text)
