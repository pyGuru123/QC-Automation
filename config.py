import os
from src.bucketing import BUCKET

# SET EMAIL COLUMN
EMAIL_COLUMN = 5

# EXCEL FILE LOCATION
DATA_FILE = "sample_data/MILKMAN_SAMPLE_6THFEB.xlsx"

# GROUPED MATCHING
REQUIRED_COLUMNS = ['First Name', 'Company', 'Phone', 'Email']

INDUSTRIES = ['dairy','food & beverages']
INDUSTRIES = list(map(lambda x : x.lower(), INDUSTRIES))

LOCATIONS = ['Delhi', 'Punjab', 'Maharashtra', 'Karnataka', 'Telangana', 'Gujarat', 'Rajasthan',
            'Andhra Pradesh']
LOCATIONS = list(map(lambda x : x.lower(), LOCATIONS))

# SAMPLE QUANTITY LENGTH
SAMPLE_LENGTH = 20

# EMPLOYEES RANGE
MIN_EMP = 4
MAX_EMP = 200