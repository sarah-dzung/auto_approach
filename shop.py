import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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
    shop_items = driver.find_elements(By.XPATH, "//*[contains(@class, 'add-to-cart-button')]")

    for item in shop_items:
        time.sleep(1)
        item.click()


class Product:
    def __init__(self, name: str, price: float, cart_button: WebElement):
        self.name = name
        self.price = price
        self.cart_button = cart_button


class Cart:
    def __init__(self):
        self.products = {}
        

    def add_product(self, product: Product) -> None:
        # Add new product to cart
        if product in self.products:
            self.products[product] += 1 
            product.cart_button.click()
        else:
            self.products[product] = 1



    def add_new(self, product):
        """
        Add a product to cart that is not already in the cart
        """
        self.products[product] += 1


    def update_qty(self, product):
        """
        Update the quantity of a product that already exists in the cart
        """
        self.products[product] = 1

        



    
