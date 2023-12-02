from selenium import webdriver
import my_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import *

timeout = 10

def login(driver: webdriver) -> bool:
    print("Logging in...\t\t", end="")
    driver.get("https://oneup.approach.app/login")

    email_element = find_element(driver, (By.ID, 'login-email'))
    if not email_element:
        print("Error: Unable to locate email field.")
        return False
    
    password_element = find_element(driver, (By.ID, 'login-password'))
    if not password_element:
        print("Error: Unable to locate password field.")
        return False
    
    login_button = find_clickable_element(driver, (By.XPATH, "//span[contains(@class, 'MuiButton-label') and contains(text(), 'Log In')]"))
    if not login_button:
        print("Error: Unable to locate log in button.")
        return False

    email_element.send_keys(my_login.email)
    password_element.send_keys(my_login.password)
    login_button.click()
    print("Done")
    return True


def set_location(driver: webdriver) -> bool:
    print("Setting location...\t", end="")
    location_button = find_clickable_element(driver, (By.XPATH, "//div[contains(@class, 'MuiButtonBase-root') and .//span[text()='One Up Bouldering']]"))
    if not location_button:
        print("Error: Could not locate location option for 1UP.")
        return False
    
    location_button.click()
    print("Done")
    return True


def set_device(driver: webdriver) -> bool:
    print("Setting device...\t", end="")
    device_button = find_clickable_element(driver, (By.XPATH, "//ul[contains(@class, 'MuiList-root')]/div[contains(@class, 'MuiButtonBase-root')][1]"))
    if not device_button:
        print("Error: Could not find device option.")
        return False
    
    device_button.click()
    print("Done")
    return True



    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        print("Error: Unable to load dashboard: Daily checkins not displaying.")
