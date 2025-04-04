import pandas as pd
sales = pd.read_csv("data manipulation w pandas/aggregating_dataframes/sales.csv")

# Print the head of the sales DataFrame
print(sales.tail())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())