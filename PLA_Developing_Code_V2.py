# Imports modules for CSV and Randomization
import csv
import random as rd
from random import randint
import json
import pandas as pd
import os

# # Imports Addresses coming from a csv to be randomize over 47.000 addresses
def PandasExporting():
    csvfile = 'addresses.csv'
    pandasread = pd.read_csv(csvfile,sep= 'delimiter', header=None)
    print(pandasread)
PandasExporting()

