from Base.Base_Test import BaseTest

from Pages.Login_Page import LoginPage
from Pages.Open_Checking_Page import OpenCheckingPage

from Utils.Config import Config


class TestChecking(BaseTest):

    def test_open_checking_account(self):

        self.driver.get(
            Config.URL
        )

        login_page = LoginPage(
            self.driver
        )

        login_page.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        checking_page = OpenCheckingPage(
            self.driver
        )

        checking_page.open_checking_account()

        print(
            "Open Checking Account Successful"
        )