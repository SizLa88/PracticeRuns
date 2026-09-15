import sys
import os

# FIXED: Natively forces path resolution so 'Base' and 'Utils' resolve perfectly across all 4 workers
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Now declare your framework and package module imports cleanly
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from Utils.Screenshot_Helper import ScreenshotHelper


@pytest.fixture(scope="function", autouse=True)
def setup_driver(request):
    """
    Initializes a thread-safe, headless browser instance compatible with pytest-xdist parallel workers.
    """
    edge_options = EdgeOptions()

    # HARDCODED HEADLESS ENGINE: Forces headless execution implicitly to bypass CLI crashes
    edge_options.add_argument("--headless=new")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--window-size=1920,1080")
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(10)

    # Bind the driver dynamically to the test class instance to allow screenshot interception
    if request.cls is not None:
        request.cls.driver = driver

    request.node.driver = driver

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Listens for test failures and snaps screenshots cleanly across thread workers.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if not driver and hasattr(item, "instance") and item.instance is not None:
            driver = getattr(item.instance, "driver", None)

        if driver:
            try:
                safe_name = f"FAIL_{item.name.replace('[', '_').replace(']', '_')}"
                ScreenshotHelper.take_screenshot(driver, safe_name)
            except Exception as e:
                print(f"\n[SCREENSHOT ERROR] Unable to capture diagnostic screenshot: {e}")
