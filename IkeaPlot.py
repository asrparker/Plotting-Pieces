import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from the csv file
df = pd.read_csv("C:\Adam\Experiment Data\AntiCrush\Crush_Test\data_threshHeavy.csv")

# Select the column you want to plot and generate the trendline for
x = df[" Sum"]

# Get the last 10% of the data
# section = int(0.6 * len(x))
# x = x[:section]
# x = x[-section:]

# Perform linear regression to generate the slope and intercept of the trendline
slope, intercept, _, _, _ = linregress(np.arange(len(x)), x)

# Generate the y-values for the trendline
trendline_y = slope * np.arange(len(x)) + intercept

# Plot the values and the trendline
plt.plot(np.arange(len(x)), x, '.', label='data')
plt.plot(np.arange(len(x)), trendline_y, label='trendline')
plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Trendline Plot')
plt.show()