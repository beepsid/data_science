# Import cars data
import pandas as pd
cars = pd.read_csv('C:\study\github\data_science\python_intermediate\pandas\cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars[['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars[['cars_per_cap', 'drives_right']])
