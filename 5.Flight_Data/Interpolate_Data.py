"""
This program reads data from .csv files, interpolates it to get a smooth curve, and saves it to a .csv file.
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
    HTL_fd = read_data('5.Flight_Data/1.Flight_Data_relevant/tc74s.csv', [2,3,4,5,6,7])
    Temps_fd = read_data('5.Flight_Data/1.Flight_Data_relevant/pt1000s.csv', [2,3,6,9,12,15,18,2])

    ## Interpolate data
    HTL_fd_interp = interpolate_data(HTL_fd,500)
    #print(HTL_fd_interp)
    Temps_fd_interp = interpolate_data(Temps_fd,500)
    ## Save data
    save_data(HTL_fd_interp, '5.Flight_Data/1.Flight_Data_relevant/tc74s_interp.csv')
    save_data(Temps_fd_interp, '5.Flight_Data/1.Flight_Data_relevant/pt1000s_interp.csv')
#
#%% Read data ##################################################################
def read_data(filename, ncols):
    """
    Reads data from a .csv file and returns a numpy array
    Inputs: 
        - filename - the name of the file to be read
        - ncols - the number of columns in the file as a list []
    """
    data = pd.read_csv(filename, usecols=ncols)
    return data#.values

#%% Interpolate data ##########################################################
#def interpolate_data(data): #NEEDS FIXING
#    """
#    Interpolates data to get a smooth curve using scipy.interpolate.BSpline
#    Inputs: 
#       - data - the data to be interpolated, the first column is the time, the rest are the values. Interpolate for each column separately
#       Ignore the time column
#    """
#    #data_interp = np.zeros((data.shape[0], data.shape[1]))
#    #data_interp[:, 0] = data[:, 0]
#    #for i in range(1, data.shape[1]):
#    #    tck = BSpline(data[:, 0], data[:, i], k=3)
#    #    data_interp[:, i] = splev(data_interp[:, 0], tck, der=0)
#    #return data_interp
#    data_interp = np.zeros((data.shape[0], data.shape[1]))
#    data_interp[:, 0] = data[:, 0]
#    for i in range(1, data.shape[1]):
#        data_interp[:, i] = np.interp(
#            data_interp[:, 0], data[:, 0], data[:, i])
#    return data_interp

def interpolate_data(data,window=100):
    """ 
    Use pandas rolling method to take the moving average of specific columns of a pandas dataset. 
    """
    # Create a new dataframe with the moving average of the columns
    data_interp = pd.DataFrame(index=data.index)
    data_interp[data.columns[0]] = data[data.columns[0]]
    for i in range(1, data.shape[1]):
        data_interp[data.columns[i]] = data[data.columns[i]].rolling(window=window).mean()
    return data_interp.values

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
