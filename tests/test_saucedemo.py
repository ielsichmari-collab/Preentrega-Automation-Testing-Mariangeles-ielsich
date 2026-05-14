import pytest
from selenium.webdriver.common.by import By
from utils.functions import configurar_navegador

@pytest.fixture
def driver():
    # Inicializa y cierra navegador
    browser = configurar_navegador()
    yield browser
    browser.quit()

def test_pre_entrega_saucedemo(driver):
    # Navegacion y Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Validacion de URL y Logo
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs"
    
    # Verificacion de Catalogo (Criterios Minimos)
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0 # Valida presencia de productos
    
    # Extraer Nombre y Precio del primero (Criterio Minimo)
    primer_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\nProducto: {primer_nombre} | Precio: {primer_precio}")

    # Validar elementos de interfaz (Menu y Filtros)
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    
    # Flujo de Carrito (Agregar y Validar Badge)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"
    
    # Validar Carrito y Producto Agregado
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()        
    assert "cart.html" in driver.current_url
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1
    cart_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_nombre == primer_nombre
    
    
    

    
    
    
    