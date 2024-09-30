#this file contains logic for classifying customers into high,medium and low segments
#usinf customer_csv file.

import pandas as pd

from sympy import false

#Reading the dataset
df = pd.read_csv(r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\customer_data.csv')

def segment_customers(row):
    if row['annual_income'] > 60000 and row['loyalty_score'] > 6.5 and row['purchase_frequency'] > 23.5:
        return 'High customer'
    elif row['annual_income'] > 45000 and row['loyalty_score'] > 4.5 and row['purchase_frequency'] > 14.5:
        return 'Medium customer'
    else:
        return 'Low customer'

#Apply segmentation to logic
df['segment'] = df.apply(segment_customers, axis=1)

#Saving the updated DataFrame to a new Excel spreadsheet
df.to_excel('customer_segregation,xlsx', index = False)