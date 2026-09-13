from Base.Base_Test import BaseTest

from Pages.Login_Page import LoginPage

from Utils.Config import Config


class TestLogin(BaseTest):

    def test_login(self):

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

        print(
            "Login Successful"
        )