import time
import sys
import os
import pickle
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import setup_session
from helper import *
from shop import *

chrome_options = Options()
chrome_options.add_argument("--window-size=1680,1200")
driver = Chrome(chrome_options)
driver.get("http://oneup.approach.app/login")
    
if not setup_session.login(driver):
    sys.exit("Unable to login.")

if not setup_session.set_location(driver):
    sys.exit("Unable to set location.")

if not setup_session.set_device(driver):
    sys.exit("Unable to set device.")

if not find_element(driver, (By.XPATH, "//span[contains(text(), \"Today's Checkins\")]")):
    sys.exit("Unable to load dashboard.")


SHOP_URL = "https://oneup.approach.app/store/shop?locationId=1&searchString=&pageSize=10&page=1&order=ASC&orderBy=name"
driver.get(SHOP_URL)

products = []

# Add all products to list
rows = find_elements(driver, (By.CLASS_NAME, 'data-table-row'))

for row in rows:
    name = driver.execute_script("return arguments[0].textContent;", row.find_element(By.CLASS_NAME, 'product-title'))
    cart_buttons = row.find_elements(By.CLASS_NAME, 'add-to-cart-button')
    if not cart_buttons:
        continue
    cart_button = cart_buttons[0]
    price = row.find_element(By.CLASS_NAME, 'price')
    product = Product(name=name, price=price, cart_button=cart_button)
    products.append(product)
    print(f"\'{product.name}\' added to products.")

def search_item(products) -> Product:
    items_found = []
    
    item_searched = input("Search shop item: ").strip()
    if item_searched == "":
        return None
    
    print(f"Item searched: {item_searched}")

    for product in products:
        if item_searched.lower() in product.name.lower():
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


cart = Cart()
item = search_item(products)
if item:
    item.cart_button.click()
    print(f"Adding '{item.name}' to cart")
    cart.add(driver, item)

cart.update_qty(driver, item, 3)
cart.update_qty(driver, item, 5)
            

"""
[x] add item to cart 
[ ] wait for item to be ready before next action
[ ] add multiple items to cart one at a time (must wait for prev item to appear before next click)
[ ] update qty of an item in the cart
"""

time.sleep(100000)
driver.quit()



"""
NOTES:
- not bothering to error check atm for if add to cart is successful
    prev check for add new item to cart: find_element(driver, (By.XPATH, f"//div[@class='cart-item']//span[@class='item-name' and contains(text(), '{product.name}')]"))


TO DO (SUGGESTION):
- Decide whether to store add to cart buttons immediately upon loading shop or one at a time as needed when product is added to cart.
- Locate and store the cart item element in cart item once an item has been added to cart
    - Advantages:
        - reduces time to update item qty
        - potentially can try to implement this to run in background while still accepting user input 
    - Disadvantges:
        - extra time to add item to cart
        - may not be worth it if most items don't get qty update
        
"""



'''
- element to update qty of cart item (contains +- buttons and number input field)
    class="cart-item-col item-ticker"
    
    
    I ran 'pip install mypy' and I believe it has installed to python3.11, however visual studio code shows that my global python interpreter is python3.12
    
    
'''

