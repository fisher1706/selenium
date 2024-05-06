import time
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get('https://www.freeconferencecall.com/global/pl')

login_button = driver.find_element("xpath", '//*[@id="login-desktop"]')
login_button.click()

email_field = driver.find_element("xpath", '//input[@id="login_email"]')
email_field.send_keys("zapel")

"""
get value el[email_field]
"""
print(email_field.get_attribute("value"))

email_field.clear()
time.sleep(2)

email_field.send_keys("fisher")
print(email_field.get_attribute("value"))
time.sleep(2)
