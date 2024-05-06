import time

from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")

url = driver.current_url
time.sleep(2)
print(url)
assert url == "https://www.wikipedia.org/", "Wrong url"

title = driver.title
print(title)

"""get page code"""
code = driver.page_source
print(code)
