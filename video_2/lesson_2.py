from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/oleg/PycharmProjects/selenium/drivers/chromedriver')
browser = webdriver.Chrome(service=service)

# browser.get('https://duckduckgo.com')
browser.get('https://app-qa.storeroomlogix.com/')
browser.find_element(By.XPATH, button_xpath).click()

# browser.save_screenshot('zapel.png')
#
# browser.refresh()
# browser.quit()


