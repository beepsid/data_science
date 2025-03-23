# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_project/netflix.csv")

# Filter for movies from the 1990s
df_90s = netflix_df[(netflix_df['release_year'] >= 1990) & 
                    (netflix_df['release_year'] < 2000) & 
                    (netflix_df['type'] == 'Movie')] 
print(df_90s)

# Plot the histogram of release years for movies from the 1990s
plt.hist(df_90s['release_year'], bins=10, edgecolor='black', color='blue')
plt.title("Movies Released in the 1990s")
plt.show()

# Get the most frequent movie duration in the 1990s and store as 'duration'
duration = df_90s['duration'].mode()[0]     
print(f"The most frequent movie duration in the 1990s is: {duration} minutes")

# Create dataframe for action movies from the 1990s
df_action = df_90s[df_90s['genre'].str.contains('Action', case=False)]
print(df_action)

# Short action movies (< 90 minutes) from the 1990s
df_short_action = df_action[df_action['duration'] < 90]
print(df_short_action)

# Count the short action movies and store as 'short_movie_count'
short_movie_count = df_short_action['show_id'].count()
print(f"Number of short action movies in the 1990s: {short_movie_count}")