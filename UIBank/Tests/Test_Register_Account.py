import pytest

from Base.Base_Test import BaseTest
from Pages.Register_Account_Page import RegisterAccountPage
from Utils.Excel_Reader import ExcelReader
from Utils.Config import Config


@pytest.mark.parametrize(
    "email,password,first_name,last_name,"
    "middle_initial,sex,title,"
    "employment_status,date_of_birth,"
    "marital_status,dependents,"
    "username,agree_terms",
    ExcelReader.get_test_data()
)
class TestRegisterAccount(BaseTest):

    def test_register_account(
            self,
            email,
            password,
            first_name,
            last_name,
            middle_initial,
            sex,
            title,
            employment_status,
            date_of_birth,
            marital_status,
            dependents,
            username,
            agree_terms
    ):

        self.driver.get(
            Config.URL
        )

        register_page = RegisterAccountPage(
            self.driver
        )

        register_page.register_new_user(
            email,
            password,
            first_name,
            last_name,
            middle_initial,
            sex,
            title,
            employment_status,
            marital_status,
            date_of_birth,
            dependents,
            username,
            agree_terms
        )

        print(
            f"Successfully Registered: {username}"
        )

        assert True