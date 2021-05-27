# Importing libraries:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Importing the os library specifically for reading the csv once I've created the file in my working directory.
import os

# Setting up the user credentials:

from env import host, user, password, get_db_url

# Telco acquire function
# SQL query pulls everything from the customers table and adds the following columns:
# Payment type, internet service type, and contract type
# This function also includes caching. If the file exists as CSV in the working directory, it will
# return that file as Pandas DataFrame. If it does not exist, it will run the SQL query and write it
# as a CSV to the working directory.

def get_telco_data():
    
    my_telco_query = '''SELECT c.*, pt.payment_type, ist.internet_service_type, ct.contract_type
                FROM customers as c
                JOIN payment_types as pt on c.payment_type_id = pt.payment_type_id
                JOIN internet_service_types AS ist on ist.internet_service_type_id = c.internet_service_type_id
                JOIN contract_types as ct ON ct.contract_type_id = c.contract_type_id;'''
    
    
    filename = 'telco_data.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        telco_df = pd.read_sql(my_telco_query, get_db('telco_churn'))
        telco_df.to_csv(filename, index = False)
        
    return telco_df