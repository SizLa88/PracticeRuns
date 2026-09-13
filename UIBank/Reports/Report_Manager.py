import os


class ReportManager:

    REPORT_FOLDER = "Reports"

    @staticmethod
    def create_reports_folder():

        os.makedirs(
            ReportManager.REPORT_FOLDER,
            exist_ok=True
        )

        print(
            "[REPORT] Reports folder ready."
        )
