import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from video_1.lesson_11.locators import VISIBLE_AFTER_BUTTON, ENABLE_IN_SECONDS, REMOVE_BUTTON, ENABLE_BUTTON, TEXT_FIELD

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demoqa.com/dynamic-properties")
wait = WebDriverWait(driver, 15, poll_frequency=1)

button = wait.until(EC.presence_of_element_located(VISIBLE_AFTER_BUTTON))
print(button)
button.click()

driver.refresh()

wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS)).click()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

driver.find_element(*REMOVE_BUTTON).click()
wait.until(EC.presence_of_element_located(REMOVE_BUTTON))

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))
time.sleep(10)
