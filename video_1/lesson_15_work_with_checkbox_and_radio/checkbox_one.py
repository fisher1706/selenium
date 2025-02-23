import time
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")

driver.get('https://the-internet.herokuapp.com/checkboxes')

checkbox_status_before = driver.find_element(*CHECKBOX_1).get_attribute("checked")
print(checkbox_status_before)

is_selected_before = driver.find_element(*CHECKBOX_1).is_selected()
print(is_selected_before)

time.sleep(3)
driver.find_element(*CHECKBOX_1).click()
time.sleep(3)

checkbox_status_after = driver.find_element(*CHECKBOX_1).get_attribute("checked")
print(checkbox_status_after)
print(type(checkbox_status_after))

is_selected_after = driver.find_element(*CHECKBOX_1).is_selected()
print(is_selected_after)
