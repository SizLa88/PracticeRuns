from Base.Base_Test import BaseTest
from Pages.Login_Page import LoginPage
from Pages.Transfer_Funds_Page import TransferFundsPage
from Utils.Config import Config


class TestTransferFunds(BaseTest):

    def test_transfer_funds(self):

        self.driver.get(Config.URL)

        login_page = LoginPage(
            self.driver
        )

        login_page.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        print(
            "URL AFTER LOGIN:",
            self.driver.current_url
        )

        self.driver.save_screenshot(
            "Reports\\AfterLogin.png"
        )

        transfer_page = TransferFundsPage(
            self.driver
        )

        transfer_page.transfer_funds(
            amount=Config.TRANSFER_AMOUNT,
            from_account_index=0,
            to_account_index=0
        )