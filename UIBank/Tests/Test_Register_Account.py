import pytest

from Base.Base_Test import BaseTest
from Pages.Register_Account_Page import RegisterAccountPage
from Utils.Excel_Reader import ExcelReader
from Utils.Config import Config


def get_registration_data():

    rows = ExcelReader.get_row_count()

    data = []

    for row in range(1, rows + 1):

        data.append(

            (
                ExcelReader.get_cell_data(row, 0),   # email
                ExcelReader.get_cell_data(row, 1),   # password
                ExcelReader.get_cell_data(row, 2),   # firstName
                ExcelReader.get_cell_data(row, 3),   # lastName
                ExcelReader.get_cell_data(row, 4),   # middleInitial
                ExcelReader.get_cell_data(row, 5),   # sex
                ExcelReader.get_cell_data(row, 6),   # title
                ExcelReader.get_cell_data(row, 7),   # employmentStatus
                ExcelReader.get_cell_data(row, 8),   # dateOfBirth
                ExcelReader.get_cell_data(row, 9),   # maritalStatus
                ExcelReader.get_cell_data(row, 10),  # dependents
                ExcelReader.get_cell_data(row, 11),  # username
                ExcelReader.get_cell_data(row, 12)   # agreeTerms
            )

        )

    return data


@pytest.mark.parametrize(
    "email,password,first_name,last_name,"
    "middle_initial,sex,title,"
    "employment_status,date_of_birth,"
    "marital_status,dependents,"
    "username,agree_terms",
    get_registration_data()
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
            username
        )

        print(
            f"Successfully Registered : {username}"
        )