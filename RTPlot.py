"""
Code to plot predictions and cumulants in real time
Code written by ChatGPT on Feb 15 2022
"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


# Define the function that will plot the data in real-time
def plot_real_time(prediction, load):
    # Define a fixed length of data to show in the plot
    plot_length = 50

    # Initialize the plot and set the x-axis limits
    fig, ax = plt.subplots()
    ax.set_ylim([0, 1])
    ax.set_xlim([0, plot_length])

    # Create the line object to plot the data
    line, = ax.plot([], [])

    # Create a buffer to hold the data for the plot
    buffer = np.zeros(plot_length)

    # Define a function to update the plot with new data
    def update(frame):
        # Append the new data to the buffer
        buffer[:-1] = buffer[1:]
        buffer[-1] = prediction / load

        # Update the line object with the new data
        line.set_data(np.arange(plot_length), buffer)

        # Return the line object
        return line,

    # Animate the plot with the update function and a frame interval of 50 milliseconds
    ani = animation.FuncAnimation(fig, update, interval=50, blit=True)

    # Show the plot
    plt.show()
