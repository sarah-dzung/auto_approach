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
    name = row.find_element(By.CLASS_NAME, 'product-title').text
    cart_buttons = row.find_elements(By.CLASS_NAME, 'add-to-cart-button')
    if not cart_buttons:
        continue
    cart_button = cart_buttons[0]
    price = row.find_element(By.CLASS_NAME, 'price')
    product = Product(name=name, price=price, add_to_cart_button=cart_button)
    products.append(product)


script = """
var rows = document.getElementsByClassName('data-table-row');
var data = [];
for (var i = 0; i < rows.length; i++) {
    var name = rows[i].getElementsByClassName('product-title')[0].innerText;
    var price = rows[i].getElementsByClassName('price')[0].innerText;
    var cartButtons = rows[i].getElementsByClassName('add-to-cart-button');
    if (cartButtons.length > 0) {
        cartButton = cartButtons[0];
        data.push({name: name, price: price, button: button});
    }
}
return data;
"""


# for p in products:
#     print(p.name)

driver.quit()
