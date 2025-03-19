import sys
sys.path.append("python_intermediate/matplotlib")
from data import gdp_cap, life_exp

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
from matplotlib import pyplot as plt 

plt.plot(gdp_cap,life_exp)

# Display the plot

plt.show()