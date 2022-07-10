import requests
import json
import os
import time
import datetime as dt
import shutil
import gzip
from glob import glob
# from datetime import timedelta
# from multiprocessing import cpu_count
# from multiprocessing.pool import ThreadPool
# from zipfile import ZipFile


###############################################################################
##############################Connect to website###############################
###############################################################################

# Retrieve access token
params = {   # INSERT LOGIN DATA
}
token_url = 'https://eogauth.mines.edu/auth/realms/master/protocol/openid-connect/token'
response = requests.post(token_url, data = params)
access_token_dict = json.loads(response.text)
access_token = access_token_dict.get('access_token')

# Add token bearer and header
auth = 'Bearer ' + access_token
headers = {'Authorization' : auth}


# Check if datetime works
print(dt.date.today())

# Define start and end date
start_date = dt.date(2017, 10, 1)
end_date = dt.date(2022, 7, 1)



###############################################################################
######################Download zip folders from website########################
###############################################################################

# Create loop to calculate next_day 
## In case format change needed:
## next_day = next_day.strftime("%Y%m%d")
next_date = start_date
dates = [start_date]

while next_date != end_date:
    next_date = next_date + dt.timedelta(days=1)
    dates.append(next_date)


# Submit request with updated URL to next day
## Change data_url variable to the file you want to download

for date in dates:
    data_url = "https://eogdata.mines.edu/wwwdata/viirs_products/vnf/v30//VNF_npp_d" + str(date.strftime("%Y%m%d")) + "_noaa_v30-ez.csv.gz"
    response = requests.get(data_url, headers = headers)


    # Write response to output file
    ## You can either define the output file name directly
    # output_file = 'EOG_sensitive_contents.txt'
    ## Or get the filename from the data_url variable
    output_file = os.path.basename(data_url)
    with open(output_file,'wb') as f:
        f.write(response.content)



###############################################################################
########################Extract .csv from .gz folders##########################
###############################################################################

# # Create file directory and extension
# PATH = ' '   # INSERT PATH
# EXT = '*.csv.gz'

# # Find all .gz-files in folder
# all_gz_files = [file
#                   for path, subdir, files in os.walk(PATH)
#                   for file in glob(os.path.join(path, EXT))]

# # 
# for filename in all_gz_files:
#     # data_path = "  VNF_npp_d" + str(date.strftime("%Y%m%d")) + "_noaa_v30.csv.gz"    # INSERT PATH BEFORE VNF_np[...]
#     # response = requests.get(filename, headers = headers)
#     print(filename)

#     # output_file = os.path.basename(filename)
#     with gzip.open(filename, 'rb') as f_in:
#         with open(filename+".csv", 'wb') as f_out:
#             shutil.copyfileobj(f_in, f_out)





