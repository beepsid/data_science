import pandas as pd
temperatures = pd.read_csv("data manipulation w pandas/slicing_indexing_dataframes/temperatures.csv")

#temp_by_country_city_vs_year code

temperatures['date'] = pd.to_datetime(temperatures['date'], format='mixed')

temperatures['year']=temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=('country','city'), columns=('year'))

# See the result
print(temp_by_country_city_vs_year)

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[min(mean_temp_by_city) == mean_temp_by_city])