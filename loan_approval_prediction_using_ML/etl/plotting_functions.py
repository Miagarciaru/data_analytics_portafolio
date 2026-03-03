import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator # for minor ticks
import seaborn as sns; sns.set()

def plotting_pie_chats_distributions(sizes: np.array, labels: list, title: str) -> None:
    """
        This function create a pie chart to show some percentages of a certain distribution. It receives three
        parameters: an array (called sizes) with the percentages values, a list of labels for each percentage,
        and the title of the plot.
    """
    
    # Create the pie chart
    plt.pie(sizes, labels=labels)

    # Add a title (optional)
    plt.title(title)

    # Show the plot
    plt.show()



def plotting_normalized_distribution_histogram(data_list: pd.Series, features: dict) -> None:
    """
        This functions plots the normalized distribution of a list as a histogram. This function shows 
        some statistical values of the distribution too. It receives two parameters: the list of numerical values 
        to be plotted (as a pd.Series format) and a dictionary with the information of all the features (titles,
        color bars, etc).  
    """
    xmin = data_list.min() - 0.5
    xmax = data_list.max() + 0.5

    step_size = 1.0
    bin_edges = np.arange(start=xmin, # The interval includes this value
                        stop=xmax+step_size, # The interval doesn't include this value
                        step=step_size ) # Spacing between values

    # *************
    # Main plot
    # *************
    fig, ax = plt.subplots(figsize=(8, 6))

    # x-axis label
    x_title = features['x_title']
    ax.set_xlabel(x_title,
                  fontsize=13, x=1, horizontalalignment='right' )

    # write y-axis label for main axes
    y_title = features['y_title']
    ax.set_ylabel(y_title,
                y=1, horizontalalignment='right')

    title_plot = features["title_plot"]
    ax.set_title(title_plot)

    bar_color = features["bar_color"]
    plt.hist(data_list, bins=bin_edges, color = bar_color, alpha=0.5, align="mid", density=True)

    # Calculate percentiles
    quant_25, quant_50, quant_75 = data_list.quantile(0.25), data_list.quantile(0.5), data_list.quantile(0.75)

    # Calculate mean
    mean_value = data_list.mean()

    # [quantile, opacity, length]
    statistical_values = [[quant_25, 0.8, 0.26], [quant_50, 1, 0.46], [quant_75, 0.8, 0.46], [mean_value, 1, 0.46]]

    # Plot the lines with a loop
    for i in statistical_values:
        ax.axvline(i[0], alpha = i[1], ymax = i[2], linestyle = ":")

    ax.text(quant_25, 0.27, "25th", size = 11, alpha = 0.85)
    ax.text(quant_50, 0.47, "50th", size = 12, alpha = 1)
    ax.text(quant_75, 0.47, "75th", size = 11, alpha = 0.85)
    ax.text(mean_value, 0.47, "Mean", size = 11, alpha = 0.85)
    
    ax.grid(False)
    plt.show()