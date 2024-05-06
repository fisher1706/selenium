import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")


chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
BUTTON_4 = ("xpath", "//button[@id='promtButton']")

driver.get("https://demoqa.com/alerts")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
time.sleep(2)
wait.until(EC.alert_is_present())

driver.switch_to.alert.accept()
time.sleep(2)

wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)

wait.until(EC.alert_is_present()).dismiss()
time.sleep(2)

wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
time.sleep(2)
alert = driver.switch_to.alert
alert.send_keys("Zapel")
alert.accept()
time.sleep(2)
