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

KEY_BOARD_INPUT = ("xpath", "//input[@id='target']")

driver.get('https://the-internet.herokuapp.com/key_presses?')

driver.find_element(*KEY_BOARD_INPUT).send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element(*KEY_BOARD_INPUT).send_keys("zapel")
driver.find_element(*KEY_BOARD_INPUT).send_keys(Keys.CONTROL + "A")
time.sleep(3)

driver.find_element(*KEY_BOARD_INPUT).send_keys(Keys.BACKSPACE)
time.sleep(3)
