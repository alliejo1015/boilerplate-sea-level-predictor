import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 5))  
    fig = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    resg_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    st_yr = df['Year'].min()
    end_yr = 2050
    best_fit = {'Year': [],
            'y_1': []
            }

    for year in range(st_yr, end_yr):
      best_fit['Year'] = [year for year in range(st_yr, end_yr)]
      best_fit['y_1'] = [resg_1.slope * year + resg_1.intercept for year in range(st_yr, end_yr)]

    fig = plt.plot(best_fit['Year'], best_fit['y_1'], 'k-')


    # Create second line of best fit
    resg_2 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    st_yr = 2000 #start at 2000 instead of minimum year
    end_yr = 2050
    best_fit = {'Year': [],
            'y_1': []
            }

    for year in range(st_yr, end_yr):
      best_fit['Year'] = [year for year in range(st_yr, end_yr)]
      best_fit['y_1'] = [resg_2.slope * year + resg_2.intercept for year in range(st_yr, end_yr)]

    fig = plt.plot(best_fit['Year'], best_fit['y_1'], 'g-')


    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()