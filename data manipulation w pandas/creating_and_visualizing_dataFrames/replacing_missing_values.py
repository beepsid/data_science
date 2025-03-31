import pandas as pd
avocados=pd.read_csv("data manipulation w pandas/creating_and_visualizing_dataFrames/avocado.csv")
avocados_2016=avocados[avocados["year"]==2016]

print(avocados_2016)
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()