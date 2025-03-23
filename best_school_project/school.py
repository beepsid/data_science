# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("best_school_project/school.csv")

# Preview the data
schools.head()

#best math schools
best_math_schools = schools[['school_name', 'average_math']][schools['average_math'] >= 640].sort_values(by='average_math', ascending=False)
print(best_math_schools)

#best sat schools in dataframe

schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

#best sat schools

top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by='total_SAT', ascending=False).head(10)
print(top_10_schools)

#best borough 

borough_stats = schools.groupby('borough').agg(
    num_schools=('total_SAT', 'count'),
    average_SAT=('total_SAT', 'mean'),
    std_SAT=('total_SAT', 'std')
).sort_values(by='std_SAT', ascending=False)

largest_std_dev=(borough_stats.head(1))
largest_std_dev = largest_std_dev.round(2)

print(largest_std_dev)