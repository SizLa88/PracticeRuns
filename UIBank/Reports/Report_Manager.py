from pathlib import Path


class ReportManager:

    REPORT_FOLDER = Path("Reports")

    @staticmethod
    def create_report_folder():

        ReportManager.REPORT_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def log(message):

        ReportManager.create_report_folder()

        report_file = (
            ReportManager.REPORT_FOLDER /
            "AutomationReport.txt"
        )

        with open(report_file, "a", encoding="utf-8") as report:

            report.write(f"{message}\n")
