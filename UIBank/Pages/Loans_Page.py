from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LoansPage:

    MENU = (By.ID, "dropdownMenuLink")

    LOANS_LINK = (
        By.XPATH,
        "/html/body/app-root/body/app-nav-menu/header/nav/div/div/ul/li[1]/div/a[1]"
    )

    APPLY_BUTTON = (By.ID, "applyButton")

    EMAIL = (By.ID, "email")

    AMOUNT = (By.ID, "amount")

    TERM = (By.ID, "term")

    INCOME = (By.ID, "income")

    AGE = (By.ID, "age")

    SUBMIT = (By.ID, "submitButton")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    def open_loan_application(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.MENU
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOANS_LINK
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.APPLY_BUTTON
            )
        ).click()

    def complete_loan_application(
            self,
            email,
            amount,
            term_index,
            income,
            age):

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        ).send_keys(email)

        self.driver.find_element(
            *self.AMOUNT
        ).send_keys(amount)

        Select(
            self.driver.find_element(
                *self.TERM
            )
        ).select_by_index(term_index)

        self.driver.find_element(
            *self.INCOME
        ).send_keys(income)

        self.driver.find_element(
            *self.AGE
        ).send_keys(age)

    def submit_application(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        try:

            button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )