from selenium.webdriver.common.by import By

class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    LOGO = (By.CLASS_NAME, "app_logo")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    MENU = (By.ID, "react-burger-menu-btn")
    FILTRO = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
    
    def validar_logo(self):
        return self.driver.find_element(*self.LOGO).text
    
    def validar_titulo(self):
        return self.driver.find_element(*self.TITLE).text
    
    def cantidad_productos(self):
        return len(self.driver.find_elements(*self.PRODUCTS))
    
    def obtener_primer_producto(self):
        nombre = self.driver.find_element(*self.PRODUCT_NAME).text
        precio = self.driver.find_element(*self.PRODUCT_PRICE).text
        return nombre, precio
    
    def agregar_producto(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()
    
    def obtener_badge(self):
        return self.driver.find_element(*self.BADGE).text
    
    def abrir_carrito(self):
        self.driver.find_element(*self.CART).click()
    
    def menu_visible(self):
        return self.driver.find_element(*self.MENU).is_displayed()  
    
    def filtro_visible(self):
        return self.driver.find_element(*self.FILTRO).is_displayed()
    
    def estoy_en_inventory(self):
        return "inventory.html" in self.driver.current_url