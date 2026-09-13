import os
import openpyxl


class ExcelReader:

    FILE_PATH = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "TestData",
        "RegistrationData.xlsx"
    )

    @staticmethod
    def get_cell_data(row_num, col_num):

        try:

            workbook = openpyxl.load_workbook(
                ExcelReader.FILE_PATH
            )

            sheet = workbook.active

            cell_value = sheet.cell(
                row=row_num + 1,
                column=col_num + 1
            ).value

            workbook.close()

            return (
                str(cell_value).strip()
                if cell_value is not None
                else ""
            )

        except Exception as e:

            print(
                f"Excel Read Error: {e}"
            )

            return ""

    @staticmethod
    def get_row_count():

        try:

            workbook = openpyxl.load_workbook(
                ExcelReader.FILE_PATH
            )

            sheet = workbook.active

            row_count = sheet.max_row - 1

            workbook.close()

            return row_count

        except Exception as e:

            print(
                f"Excel Read Error: {e}"
            )

            return 0

    @staticmethod
    def get_test_data():

        try:

            print("\n========== EXCEL DEBUG ==========")

            print(
                f"Excel Path: {ExcelReader.FILE_PATH}"
            )

            if not os.path.exists(
                    ExcelReader.FILE_PATH):

                print(
                    "ERROR: Excel file not found!"
                )

                return []

            workbook = openpyxl.load_workbook(
                ExcelReader.FILE_PATH
            )

            sheet = workbook.active

            print(
                f"Worksheet: {sheet.title}"
            )

            print(
                f"Rows Found: {sheet.max_row}"
            )

            print(
                f"Columns Found: {sheet.max_column}"
            )

            data = []

            for row in sheet.iter_rows(
                    min_row=2,
                    values_only=True):

                if not any(row):
                    continue

                record = tuple(

                    "" if value is None
                    else str(value).strip()

                    for value in row

                )

                data.append(
                    record
                )

            workbook.close()

            print(
                f"Records Loaded: {len(data)}"
            )

            print(
                "================================\n"
            )

            return data

        except Exception as e:

            print(
                f"Excel Read Error: {e}"
            )

            return []