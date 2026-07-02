import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def configurar_navegador():

    logging.info("Se inicia el navegador Chrome")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    driver.implicitly_wait(10)

    return driver







