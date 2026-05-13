# Pre-Entrega QA Automation - Mariangeles Ielsich

Proyecto de automatizacion para SauceDemo.

## Estructura
* `utils/`: Configuracion del WebDriver.
* `tests/`: Casos de prueba (Login, Inventario, Carrito).
* `reports/`: Reportes HTML de ejecucion.

## Instalacion
`pip install selenium webdriver-manager pytest pytest-html`

## Ejecucion
`python -m pytest tests/test_saucedemo.py --html=reports/reporte.html`
