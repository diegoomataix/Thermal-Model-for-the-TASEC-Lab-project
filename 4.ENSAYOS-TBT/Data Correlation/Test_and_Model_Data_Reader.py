"""
This program reads  reads data from two .csv files, one with the thermal model data
and the one with the test results. Each of the files has a certain number of columns, 
representing the nodal temperature, and of rows, each representing a reading at a 
certain time. The number of rows in each file is different.
Create a function to plot the data and save everything to np.arrays  
where one column is the model temperatures and the other the test temperatures
"""


#%% Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% Import files
