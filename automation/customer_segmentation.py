#this file contains logic for classifying customers into high,medium and low segments
#usinf customer_csv file.

import pandas as pd

#Reading the dataset
df = pd.read_csv(r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\customer_data.csv')

def segment_customers(df):
    # Define the possible categories
    categories = ['Low', 'Medium', 'High']

    # Apply segmentation logic using vectorized conditions
    conditions = [
        (df['annual_income'] > 60000) & (df['loyalty_score'] > 6.5) & (df['purchase_frequency'] > 23.5),
        (df['annual_income'] > 45000) & (df['loyalty_score'] > 4.5) & (df['purchase_frequency'] > 14.5)
    ]

    # Initialize the 'segment' column with predefined categories
    df['segment'] = pd.Categorical(['Low'] * len(df), categories=categories)

    # Apply conditions to classify the customers
    df.loc[conditions[0], 'segment'] = 'High'  # Mark high-segment customers
    df.loc[conditions[1], 'segment'] = 'Medium'  # Mark medium-segment customers

    return df


# Example of saving segmented data
df = pd.read_csv(r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\customer_data.csv')
segmented_df = segment_customers(df)
segmented_df.to_excel(r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\data\segmented_customers.xlsx',
                      index=False)
