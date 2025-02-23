import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

SELECT_ONE = ("xpath", "//div[@id='selectOne']")
PROF_OPTION = ("xpath", "//div[text()='Prof.']")

driver.get('https://demoqa.com/select-menu')

driver.find_element(*SELECT_ONE).click()
driver.find_element(*PROF_OPTION).click()
time.sleep(2)
