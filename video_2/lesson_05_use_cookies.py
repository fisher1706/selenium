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

    for cookie in pickle.load(open(f"{name}_cookies", "rb")):
        print(cookie)
        driver.add_cookie(cookie)

    time.sleep(5)

    driver.refresh()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
