import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

user_one = webdriver.Chrome(options=chrome_options)

LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")


user_one.get('https://hyperskill.org/login')
time.sleep(3)

user_one.find_element(*LOGIN_FIELD).send_keys("lazebaoleg@gmial.com")
user_one.find_element(*PASSWORD_FIELD).send_keys("ZAPEL")
user_one.find_element(*SUBMIT_BUTTON).click()
time.sleep(3)


user_two = webdriver.Chrome(options=chrome_options)
user_two.get('https://hyperskill.org/login')
time.sleep(3)

user_two.find_element(*LOGIN_FIELD).send_keys("lazebaoleg@gmial.com")
user_two.find_element(*PASSWORD_FIELD).send_keys("ZAPEL")
user_two.find_element(*SUBMIT_BUTTON).click()
time.sleep(3)
