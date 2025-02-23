import base64
import time

from selenium import webdriver

auth = {
        "username": "awdev",
        "password": "stage17x"
    }

# Use a valid mobile device name
mobile_emulation = {"deviceName": "iPhone 12"}  # Change to a valid device

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

mobile_emulation = {
    "deviceMetrics": {"width": 500, "height": 480, "pixelRatio": 3.0},
    # "userAgent": "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


# Start driver
driver = webdriver.Chrome(options=chrome_options)


# pass basic authorization
driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {
    "headers": {
        "Authorization": "Basic " + base64.b64encode(
            f"{auth['username']}:{auth['password']}".encode()).decode(),
        }
    }
)


# Open a website
driver.get("https://m2-live-stage-001.antoshka.ua/uk")
time.sleep(30)

# Print user agent (to verify mobile emulation)
print(driver.execute_script("return navigator.userAgent;"))

# Close browser
driver.quit()
