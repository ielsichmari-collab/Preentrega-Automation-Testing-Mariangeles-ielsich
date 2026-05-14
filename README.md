# Pre-Entrega QA Automation - Mariangeles Ielsich

Proyecto de automatización de pruebas realizado con Python, Selenium WebDriver y Pytest. 
El objetivo es validar los flujos de Login, Catálogo y Carrito en la web SauceDemo.

## Tecnologias utilizadas
* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Pytest HTML**
* **Git**

## Instalacion
Para instalar las librerías necesarias, ejecutar:
`pip install selenium webdriver-manager pytest pytest-html`

## Ejecucion
Para ejecutar los tests y generar el reporte automático:
`python -m pytest tests/test_saucedemo.py --html=reports/reporte.html`
