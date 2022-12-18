from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path='/home/oleg/PycharmProjects/selenium/drivers/chromedriver')
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(service=service, options=chrome_options)



browser.get('https://app-qa.storeroomlogix.com/')


id = 'email'
email = browser.find_element(By.ID, id)
email.send_keys('olazeba+test+oleg@agilevision.io')

password = 'password'
pas = browser.find_element(By.ID, password)
pas.send_keys('*Zapel_1706')

button = browser.find_element(By.CLASS_NAME, 'MuiButton-label')
button.click()

time.sleep(10)

browser.find_element(By.XPATH, '//*[@id="redirectButton"]').click()

browser.find_element(By.XPATH, '//*[@id="sidebar-quoted_ordered_list"]/span').click()

# browser.find_element(By.XPATH, '/html/body/div/main/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[3]/div[3]/div').click()




browser.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div[3]/button/span[1]').click()
browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/input').send_keys('zapel')
browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]/span[1]').click()

# browser.quit()



