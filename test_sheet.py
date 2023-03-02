import os
import pytest
import logging
import pandas as pd

from bucketing import BUCKET
from autologger import Logger

data_file = "sample_data/MILKMAN_SAMPLE_6THFEB.xlsx"
required_columns = ['First Name', 'Company', 'Phone', 'Email']
industries = ['dairy','food & beverages']
FAILED_ROWS = []

################ LOGGING CONFIG ###################

logger = Logger(data_file)

################ EXTERNAL TESTS ###################

@pytest.mark.skip()
def test_CanLoadBucket():
    assert len(BUCKET) == 10

@pytest.mark.skip()
def test_CanReadFile(df):
    # We are able to load file
    df = pd.read_excel(data_file)
    assert len(df.head(5)) == 5

################ TESTING CHECKLIST #################

@pytest.fixture()
def df():
    # Making df available to all tests
    df = pd.read_excel(data_file)
    return df

def test_CheckSampleLength(df, length=20):
    # Check Number of rows in excel > mentioned in requirements
    assert len(df) >= length

def test_RequiredColumnsNotEmpty(df):
    # Required Columns not empty
    passed = True
    for column in required_columns:
        nan = list(df.loc[pd.isna(df[column]), :].index)
        if nan:
            passed = False
            for index in nan:
                logger.log(logging.DEBUG, f"{index+2}, {column} value missing")

    assert passed

def test_NoDuplicateRows(df):
    # Tests if there'a duplicate values in the df based
    # on name, phone, email_id

    passed = True
    duplicated = df[df.duplicated(subset=['First Name','Phone', 'Email'], keep=False)]
    indices = duplicated.index.to_list()
    if indices:
        passed = False
        for i, index in enumerate(indices):
            logger.log(logging.DEBUG, f"{index+2}, duplicate values found for {duplicated.iloc[i]['First Name']}")

    assert passed

def test_NumberOfEmployessInRange(df, min_emp=4, max_emp=200):
    # Tests if the number of employess are in the given range

    passed = True
    notInRange = df[(df['Employees'] < min_emp ) | (df['Employees'] > max_emp)]['Employees']
    indices = notInRange.index.to_list()
    if indices:
        passed = False
        for i, index in enumerate(indices):
            logger.log(logging.DEBUG, f"{index+2}, Number of employess not in Range({min_emp},{max_emp})")

    assert passed

def test_MatchIndustries(df):
    # Tests if the industry column is in allowed industries

    passed = True
    invalid_ind = df[~df['Industry'].isin(industries)]
    indices = invalid_ind.index.to_list()
    if indices:
        passed = False
        for i, index in enumerate(indices):
            logger.log(logging.DEBUG, f"{index+2}, {invalid_ind.iloc[i]['Industry']} is not in allowed industries")

    assert passed