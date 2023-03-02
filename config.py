import os
from bucketing import BUCKET

# SET EMAIL COLUMN
email_column = 5

# EXCEL FILE LOCATION
DATA_FILE = "sample_data/MILKMAN_SAMPLE_6THFEB.xlsx"

# GROUPED MATCHING
REQUIRED_COLUMNS = ['First Name', 'Company', 'Phone', 'Email']
INDUSTRIES = ['dairy','food & beverages']

# SAMPLE QUANTITY LENGTH
SAMPLE_LENGTH = 20

# EMPLOYEES RANGE
MIN_EMP = 4
MAX_EMP = 200