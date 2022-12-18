from selenium import webdriver
import pickle
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/user/PycharmProjects/selenium/drivers/chromedriver')

browser = webdriver.Chrome(service=service)
browser.get('https://b4g-akk.ru/register')

for cookie in pickle.load('session', 'rb'):
    browser.add_cookie(cookie)

print('cookie load')
browser.refresh()
