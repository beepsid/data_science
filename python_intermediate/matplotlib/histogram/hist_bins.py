import sys
sys.path.append("python_intermediate/matplotlib")
from data import life_exp

# Build histogram with 5 bins
from matplotlib import pyplot as plt 
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()