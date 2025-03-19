import sys
sys.path.append("python_intermediate/matplotlib")
from data import gdp_cap, life_exp
from matplotlib import pyplot as plt

# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)
plt.show()
plt.clf()

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.scatter(gdp_cap,life_exp)

# Show plot
plt.show()