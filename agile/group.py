from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import Select



service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(service=service, options=options)

browser.get('https://hub.qa.integrationlogix.com/')
email = browser.find_element(By.NAME, 'email')
email.send_keys('olazeba+ilx+qa@agilevision.io')

passwd = browser.find_element(By.NAME, 'password')
passwd.send_keys('*Zapel_1706')

button = browser.find_element(By.CLASS_NAME, 'MuiButton-label')
button.click()
time.sleep(5)









browser.find_element(By.XPATH, '//*[@id="sidebar-item-access"]').click()
el = browser.find_element(By.XPATH, '//*[@id="sidebar-item-access"]')
print(el.get_attribute('class'))


