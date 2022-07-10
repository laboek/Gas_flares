# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:06:45 2022

@author: laura
"""

# 1)
# sort through EOG VIIRS VNF data
# find Temp_BB (IR source temperature in K) between 1600K and 2200K
# include only locations between 25°-39°N and 39°-61°E (Iran / Iraq area)
# save in new .csv files (one per year 2017-2022)
# filter by coordinates (to show data through time at any one location)

# 2)
# search for highest radiances
# explore if these flare stacks are sometimes on / off


#############################################################################
#############################################################################

import pandas as pd

data_path = " "    # INSERT PATH
file = pd.read_csv(data_path)



                
            