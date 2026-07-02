import pytest
from selenium.webdriver.common.by import By
from pages import login_page
from pages import inventory_page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_producto_en_carrito(driver):
    # Navegacion y Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    
    # Validacion de URL y Logo
    assert inventory_page.estoy_en_inventory()
    assert inventory_page.validar_logo() == "Swag Labs"
    
    # Verificacion de Catalogo (Criterios Minimos)
    assert inventory_page.validar_titulo() == "Products"
    assert inventory_page.cantidad_productos() > 0 # Valida presencia de productos
    
    # Extraer Nombre y Precio del primero (Criterio Minimo)
    primer_nombre, primer_precio = inventory_page.obtener_primer_producto()
    print(f"\nProducto: {primer_nombre} | Precio: {primer_precio}")

    # Validar elementos de interfaz (Menu y Filtros)
    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()
    
    # Flujo de Carrito (Criterios Obligatorios)
    # 1. Agregar producto
    inventory_page.agregar_producto()
    
    # 2. Verificar que el contador (badge) se incremente
    assert inventory_page.obtener_badge() == "1"
    
    # 3. Navegar al carrito de compras
    inventory_page.abrir_carrito()
    cart_page = CartPage(driver)
    
    # 4. Comprobar que el producto este presente en el carrito
    assert cart_page.estoy_en_carrito()
    item_en_carrito = cart_page.obtener_producto()
    assert item_en_carrito == primer_nombre
    print(f"Confirmado: {item_en_carrito} está en el carrito.")
 
def test_catalogo(driver):    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    
    assert inventory_page.estoy_en_inventory()
    assert inventory_page.validar_logo() == "Swag Labs"
    assert inventory_page.validar_titulo() == "Products"
    assert inventory_page.cantidad_productos() > 0
    
    nombre, precio = inventory_page.obtener_primer_producto()

    print(f"Producto: {nombre} - {precio}")
    
def test_agregar_producto(driver):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    inventory_page.agregar_producto()

    assert inventory_page.obtener_badge() == "1"