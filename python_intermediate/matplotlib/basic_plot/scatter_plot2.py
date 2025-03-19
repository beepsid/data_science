
# Import package
import sys
sys.path.append("python_intermediate/matplotlib")
from matplotlib import pyplot as plt
from data import life_exp,pop2

# Build Scatter plot
plt.scatter(pop2,life_exp)

# Show plot
plt.show()