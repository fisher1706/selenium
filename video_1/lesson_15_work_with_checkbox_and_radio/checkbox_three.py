import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

driver = webdriver.Chrome(options=chrome_options)

ELEMENT_ONE = ("xpath", "//li[text()='Cras justo odio']")

driver.get('https://demoqa.com/selectable')

before = driver.find_element(*ELEMENT_ONE).get_attribute("class")
print(before)

driver.find_element(*ELEMENT_ONE).click()

after = driver.find_element(*ELEMENT_ONE).get_attribute("class")
print(after)
