from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


service = Service('/home/user/PycharmProjects/selenium/drivers/geckodriver')

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.headless = True

browser = webdriver.Firefox(service=service, options=option)
browser.get('https://nick-name.ru/generate')

while True:
    button_xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element(By.XPATH, button_xpath).click()

    link = browser.find_element(By.ID, 'register').get_attribute('href')[37:]
    print(f'Nickname: {link}')




