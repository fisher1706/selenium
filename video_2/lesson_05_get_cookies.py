import pickle
import time

import chromedriver_autoinstaller
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from auth_data import user_name, user_password, name, password

chromedriver_autoinstaller.install()

url = "https://instagram.com/"

user_agent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(5)

    username_input = driver.find_element(By.NAME, user_name)
    username_input.clear()
    username_input.send_keys(name)
    time.sleep(2)

    password_input = driver.find_element(By.NAME, user_password)
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(2)

    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    pickle.dump(driver.get_cookies(), open(f"{name}_cookies", "wb"))
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
