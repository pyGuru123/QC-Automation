import os
from pathlib import Path
import pandas as pd
from src.bucketing import BUCKET

# EXCEL FILE LOCATION
parent_dir = os.path.dirname(os.path.abspath(__file__)).strip('src\\')
test_file = os.path.join(parent_dir, 'setup.txt')

with open(test_file, 'r') as f:
    FILE_PATH = Path(f.readline())

# with open('setup.txt') as file:
#     FILE_PATH = file.readline()

df = pd.read_excel(FILE_PATH, sheet_name = 0)

def splitByComma(string):
    if str(string) != 'nan':
        return list(map(lambda x : x.strip().lower(), string.split(',')))
    return []

# REQUIRED COLUMNS MATCHING
REQUIRED_COLUMNS = ['First Name', 'Company', 'Phone No', 'Work Email']

# INDUSTRIES
INDUSTRIES = splitByComma(df.loc[0, 'Industry'])

# LOCATION
CITY = splitByComma(df.loc[0, 'City'])
STATE = splitByComma(df.loc[0, 'State'])
COUNTRY = splitByComma(df.loc[0, 'Country'])

# DESIGNATION & BUCKETS
DESIGNATION = splitByComma(df.loc[0, 'Designation'])
DESG_BUCKET = []
for desg in DESIGNATION:
    if desg in BUCKET:
        DESG_BUCKET += BUCKET[desg]
    else:
        DESG_BUCKET.append(desg)
DESG_BUCKET = list(map(lambda x : x.lower(), DESG_BUCKET))

# SAMPLE QUANTITY LENGTH
SAMPLE_LENGTH = int(df.loc[0, 'Quantity'])

# EMPLOYEES RANGE
num_emp = df.loc[0, '# Employees']
if str(num_emp) != 'str':
    MIN_EMP, MAX_EMP = map(int, num_emp.split('-'))

# ADDITIONAL COLUMNS
ADDITIONAL_COLUMNS = splitByComma(df.loc[0, 'Additional Columns'])
ADDITIONAL_COLUMNS = list(map(lambda x : x.lower(), ADDITIONAL_COLUMNS))

df.columns = map(str.lower, df.columns)
ADDITIONAL_REQ = {}
for column in ADDITIONAL_COLUMNS:
    ADDITIONAL_REQ[column] = splitByComma(df.loc[0, column])
