from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UIBank.Utils import Config
from UIBank.Utils.Screenshot_Helper import ScreenshotHelper


def test_login():

    driver = webdriver.Edge()

    try:

        driver.maximize_window()

        driver.get(Config.URL)

        wait = WebDriverWait(driver, 10)

        # Username

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "username")
            )
        ).send_keys(Config.USERNAME)

        # Password

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        ).send_keys(Config.PASSWORD)

        # Login Button

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/app-root/body/div/app-welcome-page/div[1]/div/div[1]/div/form/div[3]/button")
            )
        ).click()

        # Privacy Policy Button

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//*[@id='mat-mdc-dialog-0']/div/div/app-agreement-popup/mat-dialog-content/div[2]/button")
            )
        ).click()

        ScreenshotHelper.take_screenshot(
            driver,
            "Login_Success"
        )

        print("Login Successful")

    except Exception as e:

        ScreenshotHelper.take_screenshot(
            driver,
            "Login_Failed"
        )

        print(f"Test Failed: {e}")

        raise

    finally:

        driver.quit()
``