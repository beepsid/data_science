import pandas as pd
temperatures = pd.read_csv("data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv")
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

temperatures_ind = temperatures.set_index('city')

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])