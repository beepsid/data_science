# Import cars data
import pandas as pd
cars = pd.read_csv('C:\study\github\data_science\python_intermediate\pandas\cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])