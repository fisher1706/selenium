from selenium import webdriver
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument('--proxy-server=45.198.186.11:14593')

service = Service(executable_path='/home/user/PycharmProjects/selenium/drivers/chromedriver')

# browser = webdriver.Chrome(service=service, options=option)
browser = webdriver.Chrome(service=service)
browser.get('https://icanhazip.com')