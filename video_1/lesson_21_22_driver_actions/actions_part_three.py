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


COLUMN_A = ("xpath", "//div[@id='column-a']")
COLUMN_B = ("xpath", "//div[@id='column-b']")


driver.get('https://the-internet.herokuapp.com/drag_and_drop')
time.sleep(2)

A = driver.find_element(*COLUMN_A)
B = driver.find_element(*COLUMN_B)

actions.drag_and_drop(A, B).perform()
time.sleep(2)


GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[3]")


driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")
time.sleep(2)

actions.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(2) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()
time.sleep(2)
