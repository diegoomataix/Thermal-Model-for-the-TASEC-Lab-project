"""
This program reads data from .csv files, reads the pressure data from pS1d1 and PS2d1 sensors 
and outputs a csv file with the average pressure data.

Note! The pressure data is in mbar.
"""
#%% Import libraries ###########################################################
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline, BSpline, splev, splrep
import csv

#%% Main #######################################################################
def main():
    """
    Main function
    """
    # Read data
    data_pS = read_data('5.Flight_Data/1.Flight_Data_relevant/pressure_sensors.csv', [2, 5, 9]) # column 1 is the time, column 2 and 3 are the pressure readings

    # Average data
    data_avg = average_data(data_pS)
#
    ## Save data
    save_data(data_avg, '5.Flight_Data/1.Flight_Data_relevant/pressure_readings.csv')

#%% Read data ##################################################################
def read_data(filename, ncols):
    """
    Reads data from a .csv file and returns a numpy array
    Inputs: 
        - filename - the name of the file to be read
        - ncols - the number of columns in the file as a list []
    """
    data = pd.read_csv(filename, usecols=ncols)
    return data.values

#%% Average data ##############################################################
def average_data(data):
    """
    Averages the data in a numpy array. Only for columns 2 and 3
    Inputs: 
        - data - the data to be averaged
    """
    data_avg = np.zeros((len(data), 2))
    data_avg[:, 0] = data[:, 0]
    for i in range(len(data)):
        data_avg[i, 1] = round((data[i, 1] + data[i, 2] )/ 2,3)

    return data_avg
    
#%% Save data ##################################################################
def save_data(data, filename):
    """
    Saves data to a .csv file
    Inputs: 
        - data - the data to be saved
        - filename - the name of the file to be saved
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

#%% Run main function #########################################################
if __name__ == '__main__':
    main()
