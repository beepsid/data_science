import pandas as pd 

avocados=pd.read_csv("data manipulation w pandas/creating_and_visualizing_dataFrames/avocado.csv")
avocados_2016=avocados[avocados["year"]==2016]

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())