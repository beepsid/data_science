import pandas as pd

temperatures = pd.read_csv('data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv')
# Look at temperatures
print(temperatures.set_index('city'))

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))