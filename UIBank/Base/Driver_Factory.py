from selenium import webdriver


class DriverFactory:

    driver = None

    @staticmethod
    def initialize_driver(browser):

        if browser.lower() == "chrome":

            DriverFactory.driver = webdriver.Chrome()

        elif browser.lower() == "edge":

            DriverFactory.driver = webdriver.Edge()

        else:

            DriverFactory.driver = webdriver.Firefox()

        DriverFactory.driver.maximize_window()

        return DriverFactory.driver

    @staticmethod
    def get_driver():

        return DriverFactory.driver

    @staticmethod
    def quit_driver():

        if DriverFactory.driver is not None:

            DriverFactory.driver.quit()

            DriverFactory.driver = None