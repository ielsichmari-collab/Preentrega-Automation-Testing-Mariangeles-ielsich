from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def configurar_navegador():
    # Setup de Chrome y Driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Espera implicita y ventana maximizada
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver








