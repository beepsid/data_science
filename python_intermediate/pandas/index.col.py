# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('C:\study\github\data_science\python_intermediate\pandas\cars.csv',index_col=0)

# Print out cars
print(cars)