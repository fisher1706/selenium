import time

from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get("https://google.com")
time.sleep(10)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

