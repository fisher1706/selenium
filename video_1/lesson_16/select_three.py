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

MULTISELECT_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")
PROF_OPTION = ("xpath", "//div[text()='Prof.']")

driver.get('https://demoqa.com/select-menu')

driver.find_element(*MULTISELECT_LOCATOR).send_keys("Gree")
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
time.sleep(2)

driver.find_element(*MULTISELECT_LOCATOR).send_keys("Black")
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
time.sleep(2)

