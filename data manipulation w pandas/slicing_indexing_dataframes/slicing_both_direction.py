import pandas as pd
temperatures = pd.read_csv("data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv")
temperatures_srt = temperatures.set_index(['country', 'city']).sort_index()

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])