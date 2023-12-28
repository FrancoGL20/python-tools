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
time.sleep(5)

# Extract all the images on the page
images = driver.find_elements(by=By.TAG_NAME, value="img")
print(f"Found {len(images)} images")

# Safe all images to disk
for image in images:
    image_url = image.get_attribute("src")
    image_name = image_url.split("/")[-1]
    with open(image_name, mode="wb") as file:
        file.write(image.screenshot_as_png)

time.sleep(5)