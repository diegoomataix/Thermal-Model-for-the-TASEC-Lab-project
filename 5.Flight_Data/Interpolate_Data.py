"""
This program reads data from .csv files, interpolates it to get a smooth curve, and saves it to a .csv file.
"""
#%% Import libraries ###########################################################
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline, BSpline
import csv

#%% Main #######################################################################
def main():
    """
    Main function
    """
    # Read data
    HTL_fd = read_data('5.Flight_Data/1.Flight_Data_relevant/tc74s.csv', [2,3,4,5,6,7])
    Temps_fd = read_data('5.Flight_Data/1.Flight_Data_relevant/pt1000s.csv', [2,3,6,9,12,15,18,2])
    #print(HTL_fd)
    # Interpolate data
    HTL_fd_interp = interpolate_data(HTL_fd)
    Temps_fd_interp = interpolate_data(Temps_fd)
    # Save data
    save_data(HTL_fd_interp, '5.Flight_Data/1.Flight_Data_relevant/tc74s_interp.csv')
    save_data(Temps_fd_interp, '5.Flight_Data/1.Flight_Data_relevant/pt1000s_interp.csv')

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

#%% Interpolate data ##########################################################
def interpolate_data(data): #NEEDS FIXING
    """
    Interpolates data to get a smooth curve using scipy.interpolate.BSpline
    Inputs: 
        - data - the data to be interpolated, the first column is the time, the rest are the values. Interpolate for each column separately
        Ignore the time column
    """
    # Interpolate using scipy.interpolate.BSpline for each column
    for i in range(1, data.shape[1]):
        x = np.array(range(len(data)))
        spl = make_interp_spline(x, data, k=3)
        xnew = np.linspace(0, len(data)-1, 300)
        ynew = spl(xnew)
    return xnew, ynew

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
