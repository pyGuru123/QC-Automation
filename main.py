import subprocess
import openpyxl

from config import DATA_FILE, email_column

# REMOVE ROWS FROM EXCEL WHERE COMPANY MAIL DOESN'T EXIST

workbook = openpyxl.load_workbook(DATA_FILE)
sheet = workbook.active
for row in sheet.iter_rows():
    if row[email_column].value is None:
        sheet.delete_rows(row[0].row)
workbook.save(DATA_FILE)

# RUNNING TESTS
subprocess.call(['pytest'])

# FIX LOGS & HIGHLIGHTING
subprocess.call(['python', 'highlighter.py'])