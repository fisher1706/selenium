import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get('https://www.freeconferencecall.com/login')

el = driver.find_element("id", "loginformsubmit")
print(el)
print(type(el))


