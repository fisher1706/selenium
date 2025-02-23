import os
import pickle
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Selenium")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh()

time.sleep(5)
