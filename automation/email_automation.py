from typing import Any

import pandas as pd
from pandas import Series, DataFrame


import pandas as pd

#Reading the dataset
df = pd.read_csv(r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\customer_data.csv')

def filter_customers(df):
    # Filter customers with loyalty_score > 6.5 and age between 27 and 35
    filtered_df = df[(df['loyalty_score'] > 6.5) & (df['age'].between(27, 35, inclusive='both'))]
    return filtered_df

file_path = r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\data\filtered_customers.xlsx'

def save_filtered_customers(filtered_df, file_path):
    # Save the filtered customers to an Excel or CSV file
    filtered_df.to_excel(file_path, index=False)
    return save_filtered_customers

