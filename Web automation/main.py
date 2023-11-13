from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time


# Load environment variables
load_dotenv()

# Create a new Edge session
# service = Service(executable_path=os.getenv("WEB_DRIVER_PATH"))
driver = webdriver.Edge()

# Open website
driver.get(os.getenv("WEB_URL2"))

username = driver.find_element(by=By.CSS_SELECTOR, value="input#username")
username.send_keys("student")
password = driver.find_element(by=By.CSS_SELECTOR, value="input#password")
password.send_keys("Password123")
submit = driver.find_element(by=By.XPATH, value="//button[@class='btn']")
submit.click()
time.sleep(2)

actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

text = driver.find_element(by=By.TAG_NAME, value="h1")
actual_text = text.text
assert actual_text == "Logged In Successfully"

logout = driver.find_element(by=By.LINK_TEXT, value="Log out")
assert logout.is_displayed()

time.sleep(3)

print("Test completed successfully")