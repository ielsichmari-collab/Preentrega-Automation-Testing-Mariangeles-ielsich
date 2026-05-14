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
    
    # Flujo de Carrito (Criterios Obligatorios)
    # 1. Agregar primer producto
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # 2. Verificar que el contador (badge) se incremente
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"
    
    # 3. Navegar al carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 4. Comprobar que el producto esté presente en el carrito
    assert "cart.html" in driver.current_url
    item_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_en_carrito == primer_nombre
    print(f"Confirmado: {item_en_carrito} está en el carrito.")
    
    

    
    
    
    