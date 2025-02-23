import chromedriver_autoinstaller
from selenium import webdriver

from video_1.lesson_11_explicitly_implicitly.locators import VISIBLE_AFTER_BUTTON

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


driver.get("https://demoqa.com/dynamic-properties")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()
