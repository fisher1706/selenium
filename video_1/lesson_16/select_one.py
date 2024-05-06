import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import Keys

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")

driver.get('https://demoqa.com/select-menu')

driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)
