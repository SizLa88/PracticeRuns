from selenium.webdriver.common.by import By


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

    # Methods

    def click_savings_account(self):

        self.driver.find_element(
            *self.SAVINGS_ACCOUNT_TILE
        ).click()

    def enter_nickname(
            self,
            nickname):

        self.driver.find_element(
            *self.ACCOUNT_NICKNAME
        ).send_keys(
            nickname
        )

    def select_savings_account(self):

        self.driver.find_element(
            *self.SAVINGS_ACCOUNT_OPTION
        ).click()

    def submit_application(self):

        self.driver.find_element(
            *self.OPEN_ACCOUNT_BUTTON
        ).click()

    def view_accounts(self):

        self.driver.find_element(
            *self.VIEW_ACCOUNTS_BUTTON
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