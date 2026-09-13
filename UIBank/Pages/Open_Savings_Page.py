from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenSavingsPage:

    # Locators

    SAVINGS_ACCOUNT_TILE = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-accounts/div/div[1]/div/div/div[1]/div[2]"
    )

    ACCOUNT_NICKNAME = (
        By.ID,
        "accountNickname"
    )

    SAVINGS_ACCOUNT_OPTION = (
        By.XPATH,
        "//*[@id='typeOfAccount']/option[2]"
    )

    OPEN_ACCOUNT_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-account-apply/div/div[2]/form/button"
    )

    VIEW_ACCOUNTS_BUTTON = (
        By.ID,
        "viewAccounts"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Methods

    def click_savings_account(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SAVINGS_ACCOUNT_TILE
            )
        ).click()

    def enter_nickname(
            self,
            nickname):

        element = self.wait.until(
            EC.visibility_of_element_located(
                self.ACCOUNT_NICKNAME
            )
        )

        element.clear()
        element.send_keys(
            nickname
        )

    def select_savings_account(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SAVINGS_ACCOUNT_OPTION
            )
        ).click()

    def submit_application(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.OPEN_ACCOUNT_BUTTON
            )
        ).click()

    def view_accounts(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_ACCOUNTS_BUTTON
            )
        ).click()

    def open_savings_account(
            self,
            nickname):

        self.click_savings_account()

        self.enter_nickname(
            nickname
        )

        self.select_savings_account()

        self.submit_application()

        self.view_accounts()