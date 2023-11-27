import my_login
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

approach_url = "https://oneup.approach.app/"
driver.get(approach_url)

driver.implicitly_wait(10)

# Login
user = driver.find_element(By.ID, 'login-email')
user.send_keys(my_login.email)

password = driver.find_element(By.ID, 'login-password')
password.send_keys(my_login.password)

submit_button = driver.find_element(By.CLASS_NAME, 'MuiButton-label')
submit_button.click()

# Set location
location_xpath = "//div[contains(@class, 'MuiButtonBase-root') and .//span[text()='One Up Bouldering']]"
device_xpath = "//ul[contains(@class, 'MuiList-root')]/div[contains(@class, 'MuiButtonBase-root')][1]"
try:
    button = driver.find_element(By.XPATH, location_xpath)
    button.click()
except Exception as e:
    print("ERROR: Could not set location.")

# Set device
device_xpath = "//ul[contains(@class, 'MuiList-root')]/div[contains(@class, 'MuiButtonBase-root')][1]"
try:
    button = driver.find_element(By.XPATH, device_xpath)
    button.click()
except Exception as e:
    print("ERROR: Could not set device.")

time.sleep(1)

## SHOP
shop_url = "https://oneup.approach.app/store/shop"
driver.get(shop_url)

shop_items = driver.find_elements(By.XPATH, "//*[contains(@class, 'add-to-cart-button')]")

for item in shop_items:
    time.sleep(1)
    item.click()

print(shop_items)

time.sleep(10000000)

driver.quit()
