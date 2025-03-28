# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd
avocados=pd.read_csv("data manipulation w pandas/creating_and_visualizing_dataFrames/avocado.csv")

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(x='size',kind='bar')

# Show the plot
plt.show()