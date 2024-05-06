import os
import time
import chromedriver_autoinstaller
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads",
}

chrome_options.add_experimental_option("prefs", prefs)
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://the-internet.herokuapp.com/download')
time.sleep(2)
driver.find_elements("xpath", "//a")[3].click()
time.sleep(2)
