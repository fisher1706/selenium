import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_ACTION = ("xpath", "//label[@for='yesRadio']")

NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO_ACTION = ("xpath", "//label[@for='noRadio']")

driver.get('https://demoqa.com/radio-button')

print(driver.find_element(*YES_RADIO_STATUS).is_selected())
driver.find_element(*YES_RADIO_ACTION).click()
time.sleep(3)
print(driver.find_element(*YES_RADIO_STATUS).is_selected())

print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
