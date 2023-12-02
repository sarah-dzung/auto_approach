from typing import Optional, Tuple, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

TIMEOUT = 10

def find_clickable_element(driver: WebDriver, 
                               locator: Tuple[By, str], 
                               timeout: int = TIMEOUT) -> WebElement:
    element = None
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView();", element)

        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    except TimeoutException:
        print(f"Timeout: Element with locator {locator} not clickable after {timeout} seconds.")
    except NoSuchElementException:
        print(f"Error: Element with locator {locator} not found.")
    
    return element

def detect_element(driver: WebDriver, 
                   locator: Tuple[By, str], 
                   timeout: int = TIMEOUT) -> Optional[WebElement]:
    element = None
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        print(f"Timeout: Element with locator {locator} not found in {timeout} seconds.")
    except NoSuchElementException:
        print(f"Error: Element with locator {locator} not found.")
    
    return element

def find_element(driver: WebDriver, 
                   locator: Tuple[By, str], 
                   timeout: int = TIMEOUT) -> Optional[WebElement]:
    element = None
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        print(f"Timeout: Element with locator {locator} not found in {timeout} seconds.")
    except NoSuchElementException:
        print(f"Error: Element with locator {locator} not found.")
    
    return element

def find_elements(driver: WebDriver, 
                   locator: Tuple[By, str], 
                   timeout: int = TIMEOUT) -> List[WebElement]:
    elements = []
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
    except TimeoutException:
        print(f"Timeout: No elements with locator {locator} found in {timeout} seconds.")
    except NoSuchElementException:
        print(f"Error: No element with locator {locator} found.")
    
    return elements
