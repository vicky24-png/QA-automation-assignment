# saucedemo_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

EMAIL = os.getenv("SAUCE_USER", "standard_user")   # default username for saucedemo
PASSWORD = os.getenv("SAUCE_PASS", "secret_sauce")

driver = webdriver.Chrome()  # make sure chromedriver is in PATH
wait = WebDriverWait(driver, 10)
try:
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Select first product and add to cart
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item")) )
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
finally:
    time.sleep(2)
    driver.quit()
