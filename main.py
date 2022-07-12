""" Module to create dummy NPI list for testing. """

import os
from random import randint

import pandas as pd

# get number of npis from user
num_of_npis = int(input("How many NPI numbers do you want to create? "))


def create_dummy_npi():
    """create dummy NPI number of 10 chars"""
    range_start = 10 ** (10 - 1)
    range_end = (10**10) - 1
    return randint(range_start, range_end)


def create_new_list_of_dummy_npis(num):
    """returns a new list of dummy npis"""

    new_list = []

    for _ in range(num):
        npi = create_dummy_npi()
        new_list.append(npi)

    return new_list


def create_npi_csv_list(num):
    """create a csv file with a list of dummy npis"""
    npi_list = pd.DataFrame(data=create_new_list_of_dummy_npis(num), columns=["NPI"])
    desktop = os.path.expanduser("~/Desktop/")
    return npi_list.to_csv(f"{desktop}/{num_of_npis}-dummy-npi-list.csv", index=False)


# passes the postional argument into function and generates new list
create_npi_csv_list(num_of_npis)
