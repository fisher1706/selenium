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


driver.get('https://demoqa.com/nestedframes')
time.sleep(3)

driver.switch_to.frame("frame1")
time.sleep(3)
print(driver.find_element("xpath", "//body").text)

driver.switch_to.frame(0)
time.sleep(3)
print(driver.find_element("xpath", "//body").text)

driver.switch_to.parent_frame()
time.sleep(3)
print(driver.find_element("xpath", "//body").text)

driver.switch_to.default_content()
