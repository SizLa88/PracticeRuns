from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class DriverFactory:

    driver = None

    @staticmethod
    def initialize_driver(browser="edge"):

        if browser.lower() == "chrome":

            DriverFactory.driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                )
            )

        elif browser.lower() == "edge":

            DriverFactory.driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                )
            )

        elif browser.lower() == "firefox":

            DriverFactory.driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                )
            )

        else:

            raise Exception(
                f"Unsupported browser: {browser}"
            )

        DriverFactory.driver.maximize_window()

        return DriverFactory.driver

    @staticmethod
    def get_driver():

        return DriverFactory.driver

    @staticmethod
    def quit_driver():

        if DriverFactory.driver:

            DriverFactory.driver.quit()
            DriverFactory.driver = None
