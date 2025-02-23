import time
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']")
CHECKBOX_HOME_ACTION = ("xpath", "//span[@class='rct-checkbox']")

driver.get('https://demoqa.com/checkbox')

driver.find_element(*CHECKBOX_HOME_ACTION).click()
time.sleep(3)
status = driver.find_element(*CHECKBOX_HOME_STATUS).is_selected()
print(status)
