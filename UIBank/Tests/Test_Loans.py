from Base.Base_Test import BaseTest
from Pages.Loans_Page import LoansPage
from Utils.Config import Config


class TestLoans(BaseTest):

    def test_open_loan(self):

        self.driver.get(Config.URL)

        loans_page = LoansPage(self.driver)

        loans_page.open_loan_application()

        loans_page.complete_loan_application(
            email="test@example.com",
            amount="10000",
            term_index=3,
            income="50000",
            age="38"
        )

        loans_page.submit_application()

        print("Open Loan Successful")
