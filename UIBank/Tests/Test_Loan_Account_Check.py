from Base.Base_Test import BaseTest

from Pages.Login_Page import LoginPage
from Pages.Loan_Account_Check_Page import LoanAccountCheckPage

from Utils.Config import Config


class TestLoanAccountCheck(BaseTest):

    def test_loan_account_check(self):

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

        loan_page = LoanAccountCheckPage(
            self.driver
        )

        loan_page.search_loan(
            Config.LOAN_ACCOUNT_NUMBER
        )

        print(
            "Check Loan Account Status Successful"
        )