import os
import pytest

from utils.functions import configurar_navegador


@pytest.fixture
def driver(request):
    browser = configurar_navegador()

    yield browser

    # Si el test falló, guardar screenshot
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("screenshots", exist_ok=True)

        nombre = request.node.name

        browser.save_screenshot(
            f"screenshots/{nombre}.png"
        )

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)