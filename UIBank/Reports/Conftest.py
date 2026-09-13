import pytest

from Utils.Screenshot_Helper import ScreenshotHelper


@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(
        item,
        call):

    outcome = yield

    report = outcome.get_result()

    if (
            report.when == "call"
            and report.failed
    ):

        driver = (
            item.instance.driver
            if hasattr(
                item,
                "instance"
            )
            else None
        )

        if driver:

            ScreenshotHelper.take_screenshot(
                driver,
                item.name
            )
