# Import cars data
import pandas as pd
cars = pd.read_csv('C:\study\github\data_science\python_intermediate\pandas\cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])