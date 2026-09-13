from Base.Base_Test import BaseTest

from Pages.Login_Page import LoginPage
from Pages.Open_Savings_Page import OpenSavingsPage

from Utils.Config import Config


class TestSavings(BaseTest):

    def test_open_savings_account(self):

        self.driver.get(
            Config.URL
        )

        # Login

        login_page = LoginPage(
            self.driver
        )

        login_page.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        # Open Savings Account

        savings_page = OpenSavingsPage(
            self.driver
        )

        savings_page.open_savings_account(
            Config.SAVINGS_ACCOUNT_NAME
        )

        print(
            "Open Savings Account Successful"
        )
