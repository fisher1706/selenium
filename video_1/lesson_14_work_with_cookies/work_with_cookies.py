import pickle
import time
from pprint import pprint
import os
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

cookie = driver.get_cookie("country_code")
print(cookie)

cookies = driver.get_cookies()
pprint(cookies)

driver.add_cookie({
    "name": "Example",
    "value": "Fisher",
})

cookie_example = driver.get_cookie("Example")
print(cookie_example)

split_cookie_before = driver.get_cookie("split")
print(split_cookie_before)

driver.delete_cookie("split")
driver.add_cookie({
    "name": "split",
    "value": "QWERTY",
})

split_cookie_after = driver.get_cookie("split")
print(split_cookie_after)

all_cookies_before = driver.get_cookies()
driver.delete_all_cookies()
driver.add_cookie({
    "name": "split",
    "value": "QWERTY",
})

all_cookies_after = driver.get_cookies()
pprint(all_cookies_after)

"""
use cookie for login:
1. login with "LOGIN" and "PASSWORD"
"""

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
LOGIN = "lazebaoleg@gmail.com"
PASSWORD = "Zapel1706"

driver.get("https://www.freeconferencecall.com/en/us/login")

driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
driver.find_element(*SUBMIT_BUTTON).click()

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))
