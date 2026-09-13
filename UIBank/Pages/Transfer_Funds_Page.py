from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferFundsPage:

    # Locators

    PRIVACY_ACCEPT_BUTTON = (
        By.XPATH,
        "//app-agreement-popup//button"
    )

    ACCOUNTS_MENU = (
        By.XPATH,
        "/html/body/app-root/body/app-nav-menu/header/nav/div/div/ul/li[1]/a"
    )

    CHECKING_ACCOUNT = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-accounts/div/div[1]/div/div/div[2]/div/div/div/div[1]/a/strong"
    )

    TRANSFER_MONEY_BUTTON = (
        By.ID,
        "transferMoney"
    )

    FROM_ACCOUNT = (
        By.ID,
        "fromAccount"
    )

    TO_ACCOUNT = (
        By.ID,
        "toAccount"
    )

    TRANSFER_AMOUNT = (
        By.ID,
        "amountTransferred"
    )

    SUBMIT_TRANSFER_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-transfer-money/div[1]/div[2]/form/div[4]/button"
    )

    CONFIRM_TRANSFER_BUTTON = (
        By.XPATH,
        "//*[@id='exampleModal']/div/div/div[3]/button[1]"
    )

    VIEW_ACCOUNT_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-transfer-result/div[1]/div[1]/a/span"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def accept_privacy_policy(self):

        try:

            privacy_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.PRIVACY_ACCEPT_BUTTON
                )
            )

            privacy_button.click()

            print(
                "Privacy Policy Accepted"
            )

        except Exception:

            print(
                "Privacy Policy Popup Not Displayed"
            )

    def open_checking_account(self):

        print(
            f"Current URL: {self.driver.current_url}"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.ACCOUNTS_MENU
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKING_ACCOUNT
            )
        ).click()

    def click_transfer_money(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.TRANSFER_MONEY_BUTTON
            )
        ).click()

    def select_from_account(self, index):

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(
                self.FROM_ACCOUNT
            )
        )

        dropdown = Select(
            dropdown_element
        )

        self.wait.until(
            lambda driver: len(
                dropdown.options
            ) > 0
        )

        print("\nFROM ACCOUNT OPTIONS:")

        for i, option in enumerate(
                dropdown.options):
            print(f"{i}: {option.text}")

        dropdown.select_by_visible_text(
            dropdown.options[index].text
        )

    def select_to_account(self, index):

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(
                self.TO_ACCOUNT
            )
        )

        dropdown = Select(
            dropdown_element
        )

        self.wait.until(
            lambda driver: len(
                dropdown.options
            ) > 0
        )

        print("\nTO ACCOUNT OPTIONS:")

        for i, option in enumerate(
                dropdown.options):
            print(f"{i}: {option.text}")

        dropdown.select_by_visible_text(
            dropdown.options[index].text
        )

    def enter_amount(self, amount):

        amount_field = self.wait.until(
            EC.visibility_of_element_located(
                self.TRANSFER_AMOUNT
            )
        )

        amount_field.clear()

        amount_field.send_keys(
            str(amount)
        )

    def submit_transfer(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_TRANSFER_BUTTON
            )
        ).click()

    def confirm_transfer(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_TRANSFER_BUTTON
            )
        ).click()

    def return_to_accounts(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_ACCOUNT_BUTTON
            )
        ).click()

    def transfer_funds(
            self,
            amount,
            from_account_index,
            to_account_index):

        self.accept_privacy_policy()

        self.driver.save_screenshot(
            "Reports\\TransferFundsDebug.png"
        )

        self.open_checking_account()

        self.click_transfer_money()

        print(
            f"TRANSFER PAGE URL: {self.driver.current_url}"
        )

        self.select_from_account(
            from_account_index
        )

        self.select_to_account(
            to_account_index
        )

        self.enter_amount(
            amount
        )

        self.submit_transfer()

        self.confirm_transfer()

        self.return_to_accounts()

        print(
            "Transfer Funds Successful"
        )

