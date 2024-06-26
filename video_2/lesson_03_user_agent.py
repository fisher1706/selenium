"""
fake-useragent: https://pypi.org/project/fake-useragent/
"""

import random
from selenium import webdriver
import time
import chromedriver_autoinstaller
from fake_useragent import UserAgent


chromedriver_autoinstaller.install()
user_agent = UserAgent()

url_1 = "https://www.instagram.com"
url_2 = "https://stackoverflow.com"
url_3 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

user_agent_list = [
    "hello_world",
    "best_of_the_best",
    "python_today",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
    user_agent.random
]

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agent_list)}")

driver = webdriver.Chrome(
    options=options
)


try:
    driver.get(url=url_3)
    time.sleep(2)
    driver.get_screenshot_as_file("user_agent.png")
    driver.refresh()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
