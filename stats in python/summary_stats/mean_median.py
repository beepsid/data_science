# Import numpy with alias np
import numpy as np

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country']=='USA']

# Calculate mean consumption in USA
print(usa_consumption.mean())

# Calculate median consumption in USA
print(usa_consumption.median())