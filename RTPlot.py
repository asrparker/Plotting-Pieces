"""
Code to plot predictions and cumulants in real time
Code written by ChatGPT on Feb 15 2022
"""

import matplotlib.pyplot as plt
import numpy as np


def update_plot(prediction, load):
    # Initialize or update x and y data arrays
    if not hasattr(update_plot, 'x_data'):
        update_plot.x_data = np.array([0])
        update_plot.y_data1 = np.array([prediction])
        update_plot.y_data2 = np.array([load])
    else:
        update_plot.x_data = np.append(update_plot.x_data, update_plot.x_data[-1] + 1)
        update_plot.y_data1 = np.append(update_plot.y_data1, prediction)
        update_plot.y_data2 = np.append(update_plot.y_data2, load)

    # Clear the previous plot and create a new one
    plt.clf()
    plt.plot(update_plot.x_data, update_plot.y_data1, label='Prediction')
    plt.plot(update_plot.x_data, update_plot.y_data2, label='Load')
    plt.legend()

    # Set the plot limits based on the current x and y data
    plt.xlim([update_plot.x_data[0], update_plot.x_data[-1]])
    plt.ylim([min(update_plot.y_data1.min(), update_plot.y_data2.min()),
              max(update_plot.y_data1.max(), update_plot.y_data2.max())])

    # Display the updated plot
    plt.pause(0.01)
