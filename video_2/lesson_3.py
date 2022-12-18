from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service = Service(executable_path='/home/user/PycharmProjects/selenium/drivers/chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('https://youtube.com/')

html = browser.find_element(By.TAG_NAME, 'html')
for i in range(10):
    html.send_keys(Keys.DOWN)

xpath_button = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button/yt-formatted-string'
button = browser.find_element(By.XPATH, xpath_button)
button.click()

browser.quit()



