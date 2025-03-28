import pandas as pd
temperatures = pd.read_csv("data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv")

#previous code
temperatures['date'] = pd.to_datetime(temperatures['date'], format='mixed')

temperatures['year']=temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=('country','city'), columns=('year'))

# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')])

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
print(temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010'])