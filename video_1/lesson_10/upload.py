import os
import time

import chromedriver_autoinstaller
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')
time.sleep(2)
driver.find_element("xpath", "//*[@id='file-upload']").send_keys(f"{os.getcwd()}/downloads/5-Vertical.jpg")
time.sleep(2)
