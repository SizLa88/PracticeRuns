from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class RegisterAccountPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    # Locators

    REGISTER_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-welcome-page/div[1]/div/div[2]/div/button"
    )

    EMAIL = (
        By.ID,
        "email"
    )

    PASSWORD = (
        By.ID,
        "password"
    )

    FIRST_NAME = (
        By.ID,
        "firstName"
    )

    LAST_NAME = (
        By.ID,
        "lastName"
    )

    MIDDLE_NAME = (
        By.ID,
        "middleName"
    )

    SEX = (
        By.ID,
        "sex"
    )

    TITLE = (
        By.ID,
        "title"
    )

    EMPLOYMENT_STATUS = (
        By.ID,
        "employmentStatus"
    )

    MARITAL_STATUS = (
        By.ID,
        "maritalStatus"
    )

    AGE = (
        By.ID,
        "age"
    )

    DEPENDENTS = (
        By.ID,
        "numberOfDependents"
    )

    USERNAME = (
        By.ID,
        "username"
    )

    AGREE_CHECKBOX = (
        By.ID,
        "agreeCheckbox"
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        "/html/body/app-root/body/div/app-register-landing/app-register/div/div/div[2]/form/div[4]/button"
    )

    # Actions

    def click_register_button(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.REGISTER_BUTTON
            )
        ).click()

    def enter_email(self, email):

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        ).send_keys(email)

    def enter_password(self, password):

        self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        ).send_keys(password)

    def enter_first_name(self, first_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys(first_name)

    def enter_last_name(self, last_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        ).send_keys(last_name)

    def enter_middle_name(self, middle_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.MIDDLE_NAME
            )
        ).send_keys(middle_name)

    def select_sex(self, sex):

        Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.SEX
                )
            )
        ).select_by_visible_text(
            sex
        )

    def select_title(self, title):

        if title.lower() == "dr":

            title = "Mr"

        Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.TITLE
                )
            )
        ).select_by_visible_text(
            title
        )

    def select_employment_status(
            self,
            status):

        if status.lower() == "full-time":

            status = "Full-time"

        elif status.lower() == "part-time":

            status = "Part-time"

        elif status.lower() == "self-employed":

            status = "Unemployed"

        elif status.lower() == "student":

            status = "Part-time"

        Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.EMPLOYMENT_STATUS
                )
            )
        ).select_by_visible_text(
            status
        )

    def select_marital_status(
            self,
            status):

        Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.MARITAL_STATUS
                )
            )
        ).select_by_visible_text(
            status
        )

    def enter_dob(self, dob):

        self.wait.until(
            EC.visibility_of_element_located(
                self.AGE
            )
        ).send_keys(
            dob
        )

    def enter_dependents(
            self,
            dependents):

        self.wait.until(
            EC.visibility_of_element_located(
                self.DEPENDENTS
            )
        ).send_keys(
            dependents
        )

    def enter_username(
            self,
            username):

        self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        ).send_keys(
            username
        )

    def agree_terms(self):

        checkbox = self.wait.until(
            EC.visibility_of_element_located(
                self.AGREE_CHECKBOX
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkbox
        )

        try:

            checkbox.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                checkbox
            )

    def click_submit(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        ).click()

    # Full Registration Flow

    def register_new_user(
            self,
            email,
            password,
            first_name,
            last_name,
            middle_name,
            sex,
            title,
            employment_status,
            marital_status,
            dob,
            dependents,
            username):

        self.click_register_button()

        self.enter_email(email)

        self.enter_password(password)

        self.enter_first_name(first_name)

        self.enter_last_name(last_name)

        self.enter_middle_name(middle_name)

        self.select_sex(sex)

        self.select_title(title)

        self.select_employment_status(
            employment_status
        )

        self.select_marital_status(
            marital_status
        )

        self.enter_dob(dob)

        self.enter_dependents(
            dependents
        )

        self.enter_username(
            username
        )

        self.agree_terms()

        self.click_submit()
