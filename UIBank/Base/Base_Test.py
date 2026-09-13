import pytest

from Base.Driver_Factory import DriverFactory


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.driver = DriverFactory.initialize_driver("edge")

        yield

        DriverFactory.quit_driver()
