import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class RegisterAccountPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
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
        ).send_keys(
            str(email).strip()
        )

    def enter_password(self, password):

        self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD
            )
        ).send_keys(
            str(password).strip()
        )

    def enter_first_name(self, first_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys(
            str(first_name).strip()
        )

    def enter_last_name(self, last_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        ).send_keys(
            str(last_name).strip()
        )

    def enter_middle_name(self, middle_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.MIDDLE_NAME
            )
        ).send_keys(
            str(middle_name).strip()
        )

    def select_sex(self, sex):

        Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.SEX
                )
            )
        ).select_by_visible_text(
            str(sex).strip()
        )

    def select_title(self, title):

        title = str(title).strip()

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

        status = str(status).strip()

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
            str(status).strip()
        )

    def enter_dob(self, dob):

        self.wait.until(
            EC.visibility_of_element_located(
                self.AGE
            )
        ).send_keys(
            str(dob).strip()
        )

    def enter_dependents(
            self,
            dependents):

        dependents = str(
            dependents
        ).replace(
            ".0",
            ""
        )

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
            str(username).strip()
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

        time.sleep(1)

    def click_submit(self):

        submit_button = self.wait.until(
            EC.presence_of_element_located(
                self.SUBMIT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            submit_button
        )

        time.sleep(1)

        try:

            self.wait.until(
                EC.element_to_be_clickable(
                    self.SUBMIT_BUTTON
                )
            )

            submit_button.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                submit_button
            )

    # Complete Registration

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

        print(
            f"Submitting Registration For: {username}"
        )

        time.sleep(1)

        self.click_submit()

        print(
            f"Registration Submitted: {username}"
        )