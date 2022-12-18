from selenium import webdriver
from selenium.webdriver.firefox.service import Service


service = Service('/home/user/PycharmProjects/selenium/drivers/geckodriver')

option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override', 'example :)')

browser = webdriver.Firefox(service=service, options=option)
browser.get('https://xn--80agecg4bru4h.xn--p1ai/')







