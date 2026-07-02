from selenium.webdriver.common.by import By

class CartPage:

    PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE = (By.ID, "remove-sauce-labs-backpack")
    

    def __init__(self, driver):
        self.driver = driver
    
    def obtener_producto(self):
        return self.driver.find_element(*self.PRODUCTO).text
    
    def estoy_en_carrito(self):
        return "cart.html" in self.driver.current_url