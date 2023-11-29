import my_login
import shop
from shop import Product

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


# shop_url = "https://oneup.approach.app/store/shop"
shop_url = "https://oneup.approach.app/store/shop?locationId=1&searchString=&pageSize=100&page=1&order=ASC&orderBy=name"
driver.get(shop_url)

products = []

# Add all products to list
rows = driver.find_elements(By.CLASS_NAME, 'data-table-row')
for row in rows:
    name = row.find_element(By.CLASS_NAME, 'product-title').text.lower()
    cart_buttons = row.find_elements(By.CLASS_NAME, 'add-to-cart-button')
    if not cart_buttons:
        continue
    cart_button = cart_buttons[0]
    price = row.find_element(By.CLASS_NAME, 'price')
    product = Product(name=name, price=price, add_to_cart_button=cart_button)
    products.append(product)

def search_item(products) -> Product:
    items_found = []
    
    item_searched = input("Search shop item: ").lower().strip()
    if item_searched == "":
        return None

    for product in products:
        if item_searched in product.name:
            items_found.append(product)

    if len(items_found) == 1:
        return items_found[0]

    if len(items_found) == 0:
        print("No matching item found in shop.")
    else:
        print(f"Found {len(items_found)} matching items:")
        for item in items_found:
            print(item.name)

    return search_item(products)


item = search_item()
if item:
    item.button.click()
    print(f"Adding {item.name} to cart")
            
        



"""
- add item to cart
- add multiple items to cart with one request (put number in imp)
"""

time.sleep(100000)
driver.quit()
