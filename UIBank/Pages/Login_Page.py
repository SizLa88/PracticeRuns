from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-welcome-page/div[1]/div/div[1]/div/form/div[3]/button"
    )

    PRIVACY_BUTTON = (
        By.XPATH,
        "//*[@id='mat-mdc-dialog-0']/div/div/app-agreement-popup/mat-dialog-content/div[2]/button"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.PRIVACY_BUTTON)
        ).click()