from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoanAccountCheckPage:

    MENU = (
        By.ID,
        "dropdownMenuLink"
    )

    LOAN_LOOKUP = (
        By.XPATH,
        "/html/body/app-root/body/app-nav-menu/header/nav/div/div/ul/li[2]/div/a[1]"
    )

    EXISTING_BUTTON = (
        By.ID,
        "existingButton"
    )

    QUOTE_ID = (
        By.ID,
        "quoteID"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-loan/app-loan-lookup/div/div/div/form/div/div[2]/button"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    def search_loan(self, quote_id):

        self.wait.until(
            EC.element_to_be_clickable(
                self.MENU
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOAN_LOOKUP
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.EXISTING_BUTTON
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.QUOTE_ID
            )
        ).send_keys(
            quote_id
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()
