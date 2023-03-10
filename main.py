import subprocess
import openpyxl

from src.config import FILE_PATH

# REMOVE ROWS FROM EXCEL WHERE COMPANY MAIL DOESN'T EXIST
EMAIL_COLUMN = 4
def removeRowsWithEmptyEmails():
    workbook = openpyxl.load_workbook(DATA_FILE)
    sheet = workbook.active
    for row in sheet.iter_rows():
        if row[EMAIL_COLUMN].value is None:
            sheet.delete_rows(row[0].row)
    workbook.save(FILE_PATH)

# removeRowsWithEmptyEmails()

# RUNNING TESTS
subprocess.call(['pytest', 'src/test_sheet.py'])

# FIX LOGS & HIGHLIGHTING
subprocess.call(['python', 'src/highlighter.py'])