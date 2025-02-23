import time
import chromedriver_autoinstaller
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" # [normal] - default, [eager] - only doom
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)
# driver.set_window_size(1920, 1080)

driver.get("https://whatismyipaddress.com/")
time.sleep(2)
