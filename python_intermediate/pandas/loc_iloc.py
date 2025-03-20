# Import cars data
import pandas as pd
cars = pd.read_csv('C:\study\github\data_science\python_intermediate\pandas\cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])