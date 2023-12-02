import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from helper import *

def load_shop(driver):
    shop_url = "https://oneup.approach.app/store/shop"
    driver.get(shop_url)

def search_item():
    """
        - asks for user input 
        - returns string of name of matching shop item 
        - asks for input again if input does not match any items
        - 'ENTER' to cancel
    """

def buy_item(driver, item):
    shop_items = find_elements(driver, (By.XPATH, "//*[contains(@class, 'add-to-cart-button')]"))

    for item in shop_items:
        time.sleep(1)
        item.click()


class Shop:
    products = []

    def __init__(self):
        pass

    # load all of the button paths st


class Product:
    def __init__(self, name: str, price: float, cart_button: WebElement):
        self.name = name
        self.price = price
        self.cart_button = cart_button
 
# class CartItem:
#     def __init__(self, product: Product, qty: int):
#         self.product = product
#         self.qty = qty
        
#     # def get_qty(self):
#     #     return self.qty
        
#     def increment_qty(self) -> int:
#         """ Increment quantity of item in cart
#         Returns:
#             Updated item quantity
#         """
#         self.qty += 1
#         return self.qty

#     def update_qty(self, new_qty):
#         self.qty = new_qty
        


TODO: 
    - change cart items to a dictionary: (product name, CartItem)
    - add into a single function

class Cart:
    def __init__(self):
        self.items = {}
        
    def add(self, driver, product: Product) -> bool:
        # Click product's add to cart button
        #TODO: Change - don't click add to cart button if alr in cart, use side cart button instead
        product.cart_button.click()
        
        # Update item quantity
        if product.name not in self.cart: 
            self.cart[product.name] = 1
        else:
            self.cart[product.name] += 1
            
        # Check item has been added correctly on approach
        if not find_element(driver, (By.XPATH, f"//div[@class='cart-items']//span[text()='{product.name}']/../../following-sibling::div//input[@value='{self.cart[product.name]}']")):
            print(f"Error: Unable to add {product.name} to cart.")
            

    # FIXME: new name for function
    def add(self, driver: WebDriver, product: Product) -> bool:
        """
        Add a product to cart that is not already in the cart
        """
        FIXME: self.items[product] = 1

        product.cart_button.click()

        if not find_element(driver, (By.XPATH, 
                "//div[@class='cart-item']//span[@class='item-name'" \
                f"and contains(text(), '{product.name}')]")):
            print(f"Error: Unable to add {product.name} to cart.")
            return False
        

    def update_qty(self, driver: WebDriver, product: Product, new_qty: int) -> bool:
        """
        Update the quantity of a product that already exists in the cart
        """ 

        if product not in self.items: # FIXME:
            print(f"Cannot update quantity of {product.name} since it is not in cart.")
            return False
        
        self.items[product] = new_qty

        if not detect_element(driver, (By.XPATH, f"//div[contains(@class, 'cart-items')]//*[text()='{product.name}']")):
            print(f"Unable to locate '{product.name}' element in cart.")
            return False
        
        qty_input = find_element(driver, (By.XPATH, "//div[@class='cart-items']//*[last()]//input[contains(@class, 'MuiInputBase-input')]"))
        
        actions = ActionChains(driver)
        actions.double_click(qty_input)
        actions.send_keys(str(new_qty))
        actions.perform()
        
        print("Cart updated.")
        
        # Wait for update to complete
        # detect_element(driver, (B))
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        return True
        
    def check_cart_contains(driver: WebDriver, product: Product, qty: int) -> bool:
        xpath = f"//div[@class='cart-items']//span[text()='{product.name}']/../../following-sibling::div//input[@value='{qty}']"
        return find_element(driver, (By.XPATH, xpath))
        



    
