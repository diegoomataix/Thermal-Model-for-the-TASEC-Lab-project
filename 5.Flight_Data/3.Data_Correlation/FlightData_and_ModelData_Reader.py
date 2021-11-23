"""
This program reads  reads data from two .csv files, one with the thermal model data
and the one with the flight data. Each of the files has a certain number of columns, 
representing the nodal temperature, and of rows, each representing a reading at a 
certain time. The number of rows in each file is different.
Create a function to plot the data and save everything to np.arrays  
where one column is the model temperatures and the other the flight temperatures
"""
#%% Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%% Read data
def read_data(filename):
    """
    Reads data from a .csv file and returns a numpy array
    """
    data = pd.read_csv(filename, header=None)
    return data.values

#%% Plot data
def plot_data(model_data, test_data):
    """
    Plots the data from the model and the test data
    """
    plt.plot(model_data, label='Model')
    plt.plot(test_data, label='Test')
    plt.legend()
    plt.show()

#%% Main
def main():
    """
    Main function
    """
    model_data = read_data('model_data.csv')
    test_data = read_data('flight_data.csv')
    plot_data(model_data, test_data)

#%% Run main
if __name__ == '__main__':
    main()