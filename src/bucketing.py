import math
import pandas as pd

bucketing_file = "sample_data/Bucketing.xlsx"
df = pd.read_excel(bucketing_file)
BUCKET = {}

def removeNan(column):
    # Removes Nan values from a list
    return list(filter(lambda ele: str(ele) != 'nan', column))

def df_column(column):
    # Returns the df column removing Nan
    return removeNan(column.to_list())

# Adding Columns to BUCKET dictionary
columns = df.columns
for column in columns:
    BUCKET[column] = df_column(df[column])

########### BUCKET Columns ###########
# Owner
# CxO
# Director
# Partner
# Senior
# VP
# Manager
# Entry
# Training
# Unpaid