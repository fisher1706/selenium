import time
import chromedriver_autoinstaller
from fake_useragent import UserAgent
from selenium import webdriver
from multiprocessing import Pool

chromedriver_autoinstaller.install()

urls = [
    "https://www.youtube.com/watch?v=EMMY9t6_R4A&list=PLqGS6O1-DZLp1kgiQNpueIMCHRNzgHa1r&index=10",
    "https://google.com",
]


def get_data(url):
    global driver
    try:
        user_agent = UserAgent()
        options = webdriver.ChromeOptions()

        options.add_argument(f"user-agent={user_agent.random}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)
        driver.get(url=url)
        time.sleep(2)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(2)
    p.map(get_data, urls)
