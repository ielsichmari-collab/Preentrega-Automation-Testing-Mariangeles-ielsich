import pytest
import json

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def cargar_usuarios():
    with open("data/usuarios.json", encoding="utf-8") as archivo:
        return json.load(archivo)


@pytest.mark.parametrize(
    "usuario",
    [cargar_usuarios()[0]]
)
def test_login_correcto(driver, usuario):

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        usuario["username"],
        usuario["password"]
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.estoy_en_inventory()
    assert inventory_page.validar_logo() == "Swag Labs"


@pytest.mark.parametrize(
    "usuario",
    [cargar_usuarios()[1]]
)
def test_login_incorrecto(driver, usuario):

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        usuario["username"],
        usuario["password"]
    )

    assert "Username and password do not match" in login_page.obtener_mensaje_error()