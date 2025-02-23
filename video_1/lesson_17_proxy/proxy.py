"""
free proxy http://free-proxy.cz/ru/
"""

import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROXY_SERVER = '147.182.180.242:80'
# PROXY_SERVER = 'username:password@147.182.180.242:80'

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument(f"--proxy-server={PROXY_SERVER}")

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://free-proxy.cz/ru/')
time.sleep(5)
