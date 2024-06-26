import time

import chromedriver_autoinstaller
from fake_useragent import UserAgent
from selenium import webdriver

chromedriver_autoinstaller.install()

url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

user_agent = UserAgent()
options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
