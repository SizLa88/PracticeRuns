from UIBank.Base.Driver_Factory import DriverFactory


class BaseTest:

    def setup(self):

        self.driver = DriverFactory.initialize_driver("edge")

        return self.driver

    def teardown(self):

        DriverFactory.quit_driver()
