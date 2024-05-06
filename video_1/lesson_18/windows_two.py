import time

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)


driver.get('https://hyperskill.org/tracks')
time.sleep(3)

windows = driver.window_handles
driver.switch_to.window(windows[0])


driver.get('https://hyperskill.org/')
time.sleep(3)

driver.switch_to.new_window("tab")
time.sleep(3)

driver.switch_to.new_window("window")
time.sleep(3)
