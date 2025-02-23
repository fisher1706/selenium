import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business ']")
START_FREE_BUTTON_LOCATOR = ("xpath", "//a[text()='Start for Free']")

driver.get('https://hyperskill.org/tracks')
time.sleep(3)
print(driver.current_window_handle)

driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
time.sleep(3)
