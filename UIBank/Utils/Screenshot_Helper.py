from datetime import datetime
from pathlib import Path


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(driver, screenshot_name):

        try:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshots_folder = Path("Screenshots")
            screenshots_folder.mkdir(exist_ok=True)

            file_name = f"{screenshot_name}_{timestamp}.png"

            destination = screenshots_folder / file_name

            driver.save_screenshot(str(destination))

            print(f"Screenshot saved: {destination}")

        except Exception as e:

            print(f"Failed to take screenshot: {e}")