import pandas as pd
from customer_segmentation import segment_customers


#Reading the dataset
df = pd.read_csv(r'C:\Users\Ann Wangari\Desktop\Safcom_Projects\automation\customer_data.csv')

#segment customers based on loyalty score
segmented_df = segment_customers(df)

#save segmented data to a new file
df.to_excel('customer_segregation.xlsx', index=False)

