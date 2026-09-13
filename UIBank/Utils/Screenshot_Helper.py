import os
from datetime import datetime


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(driver, screenshot_name):

        screenshots_dir = "Screenshots"

        os.makedirs(
            screenshots_dir,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot_path = (
            f"{screenshots_dir}/"
            f"{screenshot_name}_"
            f"{timestamp}.png"
        )

        driver.save_screenshot(
            screenshot_path
        )

        print(
            f"Screenshot saved: {screenshot_path}"
        )

        return screenshot_path