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


MENU_ITEM_2_LOCATOR = ("xpath", "//*[@id='nav']/li[2]/a")
SUB_LIST__LOCATOR = ("xpath", "//*[@id='nav']/li[2]/ul/li[3]/a")

driver.get('https://demoqa.com/menu')


menu_item_2 = driver.find_element(*MENU_ITEM_2_LOCATOR)
sub_list_menu = driver.find_element(*SUB_LIST__LOCATOR)

actions.move_to_element(menu_item_2).pause(2).\
    move_to_element(sub_list_menu).pause(2).\
    perform()
