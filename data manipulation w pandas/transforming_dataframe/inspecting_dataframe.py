import numpy as np 
import pandas as pd

homelessness=pd.read_csv("data manipulation w pandas/transforming_dataframe/homelessness.csv")

# Print the head of the homelessness data
print(homeless.head())

# Print information about homelessness
print(homeless.info())

# Print the shape of homelessness
print(homeless.shape)

# Print a description of homelessness
print(homeless.describe())