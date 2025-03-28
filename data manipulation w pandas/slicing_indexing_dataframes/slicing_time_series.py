import pandas as pd 

# Load dataset
temperatures = pd.read_csv('data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv')

# Convert 'date' column to datetime, handling mixed formats
temperatures['date'] = pd.to_datetime(temperatures['date'], format='mixed')

# Filter for 2010-2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]
print(temperatures_bool)


# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08':'2011-02'])