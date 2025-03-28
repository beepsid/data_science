import pandas as pd
import datetime as dt
temperatures = pd.read_csv("data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv")
# Add a year column to temperatures
temperatures['date'] = pd.to_datetime(temperatures['date'], format='mixed')

temperatures['year']=temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=('country','city'), columns=('year'))

# See the result
print(temp_by_country_city_vs_year)