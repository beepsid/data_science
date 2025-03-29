# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd
avocados=pd.read_csv("data manipulation w pandas/creating_and_visualizing_dataFrames/avocado.csv")

#data for 2016

avocados_2016=avocados[avocados["year"]==2016]

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()