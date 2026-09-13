from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

    # Locators

    USERNAME_FIELD = (
        By.ID,
        "username"
    )

    PASSWORD_FIELD = (
        By.ID,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-welcome-page/div[1]/div/div[1]/div/form/div[3]/button"
    )

    AGREEMENT_BUTTON = (
        By.XPATH,
        "//*[@id='mat-mdc-dialog-0']/div/div/app-agreement-popup/mat-dialog-content/div[2]/button"
    )

    # Methods

    def enter_username(self, username):

        self.driver.find_element(
            *self.USERNAME_FIELD
        ).send_keys(
            username
        )

    def enter_password(self, password):

        self.driver.find_element(
            *self.PASSWORD_FIELD
        ).send_keys(
            password
        )

    def click_login(self):

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def accept_agreement(self):

        self.driver.find_element(
            *self.AGREEMENT_BUTTON
        ).click()

    def login(
            self,
            username,
            password):

        self.enter_username(
            username
        )

        self.enter_password(
            password
        )

        self.click_login()

        self.accept_agreement()