import pandas as pd

df = pd.read_csv('5.Flight_Data\2.Thermal_Model_Data\HTL_node_temps.csv', usecols=[3, 4, 5, 6])

print(df)