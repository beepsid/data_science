import sys
sys.path.append("python_intermediate/matplotlib")
from data import life_exp, life_exp1950

# Histogram of life_exp, 15 bins
from matplotlib import pyplot as plt 

plt.hist(life_exp,bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,bins=15)

# Show and clear plot again
plt.show()
plt.clf()