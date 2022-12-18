from selenium import webdriver
import pickle
import time
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/user/PycharmProjects/selenium/drivers/chromedriver')

browser = webdriver.Chrome(service=service)
browser.get('https://b4g-akk.ru/register')
time.sleep(100)
pickle.dump(browser.get_cookie(), open('session', 'wb'))


