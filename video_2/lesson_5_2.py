from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/user/PycharmProjects/selenium/drivers/chromedriver')

ip = '45.198.186.11'
port = 14593

option = webdriver.FirefoxOptions()
option.set_preference('network.proxy.type', 1)
option.set_preference('network.proxy.http', ip)
option.set_preference('network.proxy.http_port', port)
option.set_preference('network.proxy.https', ip)
option.set_preference('network.proxy.https_port', port)
option.set_preference('network.proxy.ssl', ip)
option.set_preference('network.proxy.ssl_port', port)

# browser = webdriver.Chrome(service=service, options=option)
browser = webdriver.Chrome(service=service)
browser.get('https://icanhazip.com')