import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)
scrolls = Scrolls(driver, actions)


EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")


driver.get('https://seiyria.com/bootstrap-slider/')
time.sleep(2)


EX_2 = driver.find_element(*EX_2_LOCATOR)
actions.scroll_to_element(EX_2).perform()
time.sleep(2)


scrolls.scroll_to_element(EX_2)
time.sleep(2)


driver.execute_script("alert('Hello')")
time.sleep(2)
