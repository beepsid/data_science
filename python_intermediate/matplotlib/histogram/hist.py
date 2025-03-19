# Create histogram of life_exp data
import sys
sys.path.append("python_intermediate/matplotlib")
from matplotlib import pyplot as plt 
from data import life_exp

plt.hist(life_exp)

# Display histogram
plt.show()