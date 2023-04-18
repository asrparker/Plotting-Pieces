"""
Code to plot predictions and cumulants in real time
Code written by ChatGPT on Feb 15 2022
"""

import matplotlib.pyplot as plt
import numpy as np


def update_plot(prediction, load, window_size=100):
    # Initialize or update x and y data arrays
    if not hasattr(update_plot, 'x_data'):
        update_plot.x_data = np.array([0])
        update_plot.y_data1 = np.array([prediction])
        update_plot.y_data2 = np.array([load])
    else:
        update_plot.x_data = np.append(update_plot.x_data, update_plot.x_data[-1] + 1)
        update_plot.y_data1 = np.append(update_plot.y_data1, prediction)
        update_plot.y_data2 = np.append(update_plot.y_data2, load)

    # Calculate the index of the first x-axis value to include in the window
    window_start = max(0, update_plot.x_data[-1] - window_size)

    # Clear the previous plot and create a new one
    plt.clf()
    plt.plot(update_plot.x_data[window_start:], update_plot.y_data1[window_start:], label='Prediction')
    plt.plot(update_plot.x_data[window_start:], update_plot.y_data2[window_start:], label='Load')
    plt.legend()

    # Set the plot limits based on the current x and y data and the window size
    plt.xlim([update_plot.x_data[window_start], update_plot.x_data[-1]])
    plt.ylim([min(update_plot.y_data1.min(), update_plot.y_data2.min()),
              max(update_plot.y_data1.max(), update_plot.y_data2.max())])

    # Display the updated plot
    plt.pause(0.01)
