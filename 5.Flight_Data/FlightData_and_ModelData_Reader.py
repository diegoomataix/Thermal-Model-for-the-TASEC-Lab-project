"""
This program reads  reads data from two .csv files, one with the thermal model data
and the one with the flight data. Each of the files has a certain number of columns, 
representing the nodal temperature, and of rows, each representing a reading at a 
certain time. The number of rows in each file is different.
Create a function to plot the data and save everything to np.arrays  
where one column is the model temperatures and the other the flight temperatures
"""
#%% Import libraries ###########################################################
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.npyio import save
import pandas as pd
from cycler import cycle

#%% Main #######################################################################
def main():
    """
    Main function
    """
    HTL_fd, Temps_fd = flight_model_data()

    #### Compare data to model ####
    # First, sort the data to be able to compare it. Might use a function
    #plot_compare_data(HTL_md[0,:], HTL_flight_data)
    #plot_compare_data(Temps_md[0,:], Temps_flight_data)

    #### Save the compared data ####
    # data = np.array([HTL_md[0,:], HTL_flight_data[0,:]])
    # save_data(data, '5.Flight_Data\3.Data_Correlation\HTL_compare_Temps.csv')

#%% Flight and Model data ###############################################################
def flight_model_data():
    """
    Reads the flight and model data and returns it and plots it separately
    """
    #### Read data (HTL) ####
    HTL_fd = read_data('5.Flight_Data/1.Flight_Data_relevant/tc74s_interp.csv', [2,3,4,5,6,7])
    # HTL_md = read_data('5.Flight_Data\2.Thermal_md\HTL_node_temps.csv')
    #### Read data (Other temps) ####
    Temps_fd = read_data(
        '5.Flight_Data/1.Flight_Data_relevant/pt1000s_interp.csv.', [2, 3, 6, 9, 12, 15, 18, 2])
    # Temps_md = read_data('5.Flight_Data\2.Thermal_md\Temps_node_temps.csv')
    #### Plot data (HTL) ####
    plot_data(HTL_fd, len(HTL_fd.columns), 'HTL Flight Data Temperatures',
              label=['TC74-0', 'TC74-1', 'TC74-2', 'TC74-3', 'TC74-4'], 
              savepath = '5.Flight_Data/1.Flight_Data_relevant/HTL_FlightTemps')
    # plot_Data(HTL_md...)
    #### Plot data (Other temps) ####
    plot_data(Temps_fd, len(Temps_fd.columns), 'Flight Data Temperatures', 
              label=['Anemometer', 'Air below', 'Air (infinite)', 'Air above', 
              'Exterior', 'Upper plate', 'Lower plate'], savepath = 
              '5.Flight_Data/1.Flight_Data_relevant/FlightTemps')
    # plot_Data(Temps_md...)
    return HTL_fd, Temps_fd # , HTL_md, Temps_md
    
#%% Read data ##################################################################
def read_data(filename, ncols):
    """
    Reads data from a .csv file and returns a numpy array
    Inputs: 
        - filename - the name of the file to be read
        - ncols - the number of columns in the file as a list []
    """
    data = pd.read_csv(filename, usecols=ncols)
    return data

#%% Plot and compare data ######################################################
def plot_compare_data(md, fd, upto1, upto2, title, label, savepath=None):
    """
    Plots the data from the model and the flight data
    """
    plt.style.use('grayscale')
    linestyle = cycle(['-', '--', ':', '=.', '-.'])
    fig, ax = plt.subplots(1, 1, figsize=(50, 25))
    #plt.rc('axes', prop_cycle=linestyle)
    ax.plot(md[md.columns[0]], md[md.columns[1:upto1]], next(linestyle))
    ax.plot(fd[fd.columns[0]], fd[fd.columns[1:upto2]], next(linestyle))
    fig.suptitle(title, fontsize=22)
    plt.xlabel('Time (s)',fontsize=16)
    plt.ylabel('Temperature $(^\circ\mathrm{C})$',fontsize=16)
    ax.axis([0, md[md.columns[0]].max(), 
            min(md[md.columns[1:upto1]].min().min(), fd[fd.columns[1:upto2]].min().min())*1.1, 
            max(md[md.columns[1:upto1]].max().max(), fd[fd.columns[1:upto2]].max().max())*1.1])
    ax.legend(label, fontsize = 12)
    ax.grid(color='k', linestyle='-', linewidth=0.5, which='major')
    ax.grid(color='grey', linestyle='--', linewidth=0.2, which='minor')
    ax.minorticks_on()
    plt.show()
    # Save plot
    fig.savefig(savepath)

#%% Plot and compare data ######################################################
def plot_data(md, upto, title, label, savepath=None):
    """
    Plots the data from the model or the flight data
    Inputs:
        - Model data (as a pandas dataframe)
        - upto - the number of rows to be plotted (-1 to plot all)
        - title - the title of the plot
        - Label (string for each of the columns)
        - Savepath (optional) - the path to save the plot to
    """
    plt.style.use('grayscale')
    linestyle = cycle(['-', '--', ':', '=.', '-.'])
    fig, ax = plt.subplots(1, 1, figsize=(50, 25))
    #plt.rc('axes', prop_cycle=linestyle)
    ax.plot(md[md.columns[0]], md[md.columns[1:upto]], next(linestyle))
    fig.suptitle(title, fontsize=22)
    plt.xlabel('Time (s)',fontsize=16)
    plt.ylabel('Temperature $(^\circ\mathrm{C})$',fontsize=16)
    ax.axis([0, md[md.columns[0]].max(), md[md.columns[1:upto]].min().min()*1.1, 
            md[md.columns[1:upto]].max().max()*1.1])
    ax.legend(label, fontsize = 12)
    ax.grid(color='k', linestyle='-', linewidth=0.5, which='major')
    ax.grid(color='grey', linestyle='--', linewidth=0.2, which='minor')
    ax.minorticks_on()
    plt.show()
    # Save plot
    fig.savefig(savepath)

#%% Save data ##################################################################
def save_data(data, filename):
    """
    Saves the data to a .csv file
    Inputs:
        - data - the data to be saved as a numpy array
        - filename - the name of the file to be saved
    To be used for the correlation analysis
    """
    np.savetxt(filename, data, delimiter=',')

#%% Run main ###################################################################
if __name__ == '__main__':
    main()
