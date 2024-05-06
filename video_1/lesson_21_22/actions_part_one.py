import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)


LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClick']")
HOVER_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='colorChangeOnHover']")

driver.get('https://testkru.com/Elements/Buttons')
time.sleep(3)

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hover_button = driver.find_element(*HOVER_CLICK_BUTTON_LOCATOR)

actions.click(left_button).perform()
time.sleep(3)

actions.double_click(double_button).perform()
time.sleep(3)

# actions.context_click(right_button).perform()
# time.sleep(3)

actions.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button).perform()
time.sleep(3)


actions.move_to_element(hover_button).perform()
time.sleep(3)
