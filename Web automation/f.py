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
driver.get(os.getenv("WEB_URL1"))
time.sleep(3)

username = driver.find_element(by=By.XPATH, value="//input[@name='email']")
username.click()
username.send_keys(os.getenv("EMAIL"))
password = driver.find_element(by=By.XPATH, value="//input[@name='password']")
password.click()
password.send_keys(os.getenv("PASSWORD"))

login=driver.find_element(by=By.XPATH, value="//button[@type='submit']")
login.click()

time.sleep(3)

print(driver.current_url)

time.sleep(3)