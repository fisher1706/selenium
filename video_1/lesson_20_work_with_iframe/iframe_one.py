import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)


FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
COPT_TEXT_LOCATOR = ("xpath", "//button[text() = 'Copy Text']")
IFRAME_LOCATOR = ("xpath", "//iframe")


driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(3)

driver.switch_to.frame("frame-one796456169")
driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys("Zapel")
time.sleep(3)

driver.switch_to.default_content()
driver.find_element(*COPT_TEXT_LOCATOR).click()
time.sleep(3)

iframe = driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(iframe)
