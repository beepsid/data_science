import pandas as pd 
sales = pd.read_csv("data manipulation w pandas/aggregating_dataframes/sales.csv")
# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())