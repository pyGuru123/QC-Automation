import os
import pytest
import logging
import pandas as pd

from src.autologger import Logger
from config import *


################ LOGGING CONFIG ###################

logger = Logger(DATA_FILE)

################ EXTERNAL TESTS ###################

@pytest.mark.skip()
def test_CanLoadBucket():
    assert len(BUCKET) == 10

@pytest.mark.skip()
def test_CanReadFile(df):
    # We are able to load file
    df = pd.read_excel(DATA_FILE)
    assert len(df.head(5)) == 5

################ TESTING CHECKLIST #################

@pytest.fixture()
def df():
    # Making df available to all tests
    df = pd.read_excel(DATA_FILE)
    return df

@pytest.mark.parametrize("length", [(SAMPLE_LENGTH)])
def test_CheckSampleLength(df, length):
    # Check Number of rows in excel > mentioned in requirements
    assert len(df) >= length

@pytest.mark.parametrize("required_columns", [(REQUIRED_COLUMNS)])
def test_RequiredColumnsNotEmpty(df, required_columns):
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
    # Tests if there'a duplicate values in the df based on name, phone, email_id

    passed = True
    duplicated = df[df.duplicated(subset=['First Name','Phone', 'Email'], keep=False)]
    indices = duplicated.index.to_list()
    if indices:
        passed = False
        for i, index in enumerate(indices):
            logger.log(logging.DEBUG, f"{index+2}, duplicate values found for {duplicated.iloc[i]['First Name']}")

    assert passed

@pytest.mark.parametrize("min_emp, max_emp", [(MIN_EMP, MAX_EMP)])
def test_NumberOfEmployessInRange(df, min_emp, max_emp):
    # Tests if the number of employess are in the given range

    passed = True
    notInRange = df[(df['Employees'] < min_emp ) | (df['Employees'] > max_emp)]['Employees']
    indices = notInRange.index.to_list()
    if indices:
        passed = False
        for i, index in enumerate(indices):
            logger.log(logging.DEBUG, f"{index+2}, Number of employess not in Range({min_emp},{max_emp})")

    assert passed

@pytest.mark.parametrize("industries", [(INDUSTRIES)])
def test_MatchIndustries(df, industries):
    # Tests if the industry column is in allowed industries

    passed = True
    invalid_ind = df[~df['Industry'].isin(industries)]
    indices = invalid_ind.index.to_list()
    if indices:
        passed = False
        for i, index in enumerate(indices):
            logger.log(logging.DEBUG, f"{index+2}, {invalid_ind.iloc[i]['Industry']} is not in allowed industries")

    assert passed

def test_MaxColumnsFilled(df):
    # Maximum columns are filled with 10% max error
    passed = True
    total_cells = len(df) * len(df.columns)
    empty_columns = df.isna().sum().sum()
    perc = (empty_columns / total_cells) * 100
    print(perc)
    if perc > 5:
        passed = False
        logger.log(logging.DEBUG, f"{-1}, {empty_columns} cells are not filled. ER = {perc:.1f}")

    assert passed

@pytest.mark.parametrize("locations", [(LOCATIONS)])
def test_LocationMatching(df, locations):
    # Matching locations based on keywords
    passed = True
    for index, row in df.iterrows():
        location = str(row['Company State']).lower()
        if location not in locations:
            passed = False
            logger.log(logging.DEBUG, f"{index+2}, location {location} not in given locations")

    assert passed


############################## NOT NEEDED FOR NOW ############################

@pytest.mark.skip()
def test_ComapanyEmailMatching(df):
    # tests if work email domain matching company website
    passed = True
    for index, row in df.iterrows():
        email = str(row['Email']).lower()
        company = str(row['Company']).lower()
        website = str(row['Website']).lower()

        company = ''.join(company.split())
        domain = email.split('@')[1].split('.')[0]
        if not (domain in company or domain in website):
            logger.log(logging.DEBUG, f"{index+2}, work email domain not matching company/website")

    assert passed