# Import cars data
import pandas as pd
cars = pd.read_csv('python_intermediate/loops/cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)