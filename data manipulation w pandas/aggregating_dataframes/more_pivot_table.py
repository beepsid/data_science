import pandas as pd
sales=pd.read_csv("data manipulation w pandas/aggregating_dataframes/sales.csv")

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(index='weekly_sales',values='department',columns='type',fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0,margins='True'))