import matplotlib.pyplot as plt
import pandas as pd
avocados=pd.read_csv("data manipulation w pandas/creating_and_visualizing_dataFrames/avocado.csv")

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x='nb_sold',y='avg_price',kind='scatter',title='Number of avocados sold vs. average price')

# Show the plot
plt.show()