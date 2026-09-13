from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.Config import Config


class OpenCheckingPage:

    OPEN_ACCOUNT = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-accounts/div/div[1]/div/div/div[1]/div[2]"
    )

    ACCOUNT_NICKNAME = (
        By.ID,
        "accountNickname"
    )

    CHECKING_ACCOUNT_TYPE = (
        By.XPATH,
        "//*[@id='typeOfAccount']/option[1]"
    )

    APPLY_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-account/app-account-apply/div/div[2]/form/button"
    )

    VIEW_ACCOUNTS = (
        By.ID,
        "viewAccounts"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    def open_checking_account(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.OPEN_ACCOUNT
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.ACCOUNT_NICKNAME
            )
        ).send_keys(
            Config.CHECKING_ACCOUNT_NAME
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKING_ACCOUNT_TYPE
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.APPLY_BUTTON
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_ACCOUNTS
            )
        ).click()
