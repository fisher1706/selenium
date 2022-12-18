from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(
    executable_path='/home/oleg/PycharmProjects/selenium/drivers/geckodriver'
)

driver.get('http://tutorialsninja.com/demo/')

search_field = driver.find_element_by_name("search")
search_field.send_keys('iphone')



time.sleep(5)

search_field.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]/span')

time.sleep(8)

add_to_cart_button.click()

shopping_cart_link = driver.find_element_by_link_text('Shopping Cart')

time.sleep(5)

shopping_cart_link.click()

assert "product 11" in driver.page_source
driver.close()






