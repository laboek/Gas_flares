# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:06:45 2022

@author: laura
"""

# 1)
# sort through EOG VIIRS VNF data
# [find Temp_BB (IR source temperature in K) between 1600K and 2200K] -> not necessary later as no 'normal' fires to confuse with
# include only locations between 29°-35°N and 42°-55°E (Iran / Iraq area)
# save in new .csv file

# 2)
# filter by coordinates (to show data through time at any one location)
# search for highest radiances
# explore if these flare stacks are sometimes on / off


#############################################################################
#############################################################################

import pandas as pd
import glob
from os.path import exists


# create empty list
gas_flares = []

# Find all .csv-files in folder
path = r'ADD PATH' 
csv_files = glob.glob(path + "/*.csv")

# Iterate through files
i = 0
for f in csv_files:
      
    # read the csv file
    df = pd.read_csv(f)
    
    # # subset dataframe based on temperature
    temp_low = df[(df["Temp_BB"]>=1600)]
    temp_high = temp_low[(temp_low["Temp_BB"]<=2200)]
    
    # subset dataframe based on location
    lat_low = df[(df["Lat_GMTCO"]>=29)]
    lat_high = lat_low[(lat_low["Lat_GMTCO"]<=35)]
    lon_low = lat_high[(lat_high["Lon_GMTCO"]>=42)] 
    lon_high = lon_low[(lon_low["Lon_GMTCO"]<=55)]

    # subset dataframe to exclude missing values
    temp_missing = lon_high[(lon_high["Temp_BB"]!=999999)]

    # subset dataframe based on cloud mask
    cloud1 = temp_missing[(temp_missing["Cloud_Mask"]!=999999)]
    cloud2 = cloud1[(cloud1["Cloud_Mask"]!=3)]
    cloud3 = cloud2[(cloud2["Cloud_Mask"]!=2)]
    
    # save to csv
    filename = "Gas Flares.csv"
    file_exists = exists(filename)
    cloud3.to_csv(filename, mode='a', header = not file_exists)
    
    print(str(round(100*i/len(csv_files)))+" %")
    i = i+1



                
            
