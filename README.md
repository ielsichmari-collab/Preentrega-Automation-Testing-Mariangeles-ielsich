# Proyecto Final QA Automation - Mariangeles Ielsich

Proyecto de automatización de pruebas realizado con Python, Selenium WebDriver y Pytest.
El objetivo es validar los principales flujos de la aplicación SauceDemo mediante pruebas automatizadas y aplicar los conceptos aprendidos durante el curso.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- Pytest HTML
- WebDriver Manager
- Git

## Funcionalidades implementadas

- Page Object Model (POM).
- Casos de prueba para Login, Catálogo y Carrito.
- Escenario negativo de login.
- Parametrización con Pytest.
- Uso de datos externos.
- Pruebas de API (GET, POST y DELETE).
- Generación automática de reporte HTML.

## Instalación

Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar todos los tests:

```bash
pytest
```

Generar reporte HTML:

```bash
pytest --html=reports/reporte.html --self-contained-html
```

## Estructura del proyecto

```
pages/
tests/
utils/
data/
reports/
screenshots/
```
