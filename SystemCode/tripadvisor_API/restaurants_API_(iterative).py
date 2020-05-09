import requests
import json
import pandas as pd
from time import sleep
from time import ctime
import os
import sys



###############
##  READ ME  ##
###############

# This script iteratively calls the tripadvisor API for RESTAURANTS.
# Use attractions_API script instead to call the API for local restaurants.
# Along with the json file containing returned list of attactions, this script also saves a log file
# of your API usage for your reference.
# Before running, ensure the following modules are installed:
# - requests
# - pandas


##################
##  HOW TO USE  ##
##################

# 1) When data collecting for one city, start by running one single iteration, such as start=0, end = 1.

# 2) Open the json file and refer to the first object. Look for the 'ranking_denominator' key. Its value
#    is the maximum number of entries for this country.

# 3) Run the script again, this time updating 'start' and 'end' to a higher value. New data is automatically
#    appended to the same file. To ensure data continuity, the 'start' value of your next run should be the
#    same as the 'end' value of your current run.

# 4) Repeat step 3 until a suitable number of entries have been collected.

# 5) Repeat steps 1-4 for all required cities.



# API call parameters
URL = r"https://tripadvisor1.p.rapidapi.com/restaurants/list"

auth = {'x-rapidapi-host' : 'tripadvisor1.p.rapidapi.com',
        'x-rapidapi-key' : '236421c8cdmsh773fb608a59916ep1f911bjsna4bb5067e752'}


param = {
    # Language
    "lang": "en_US",
    
    # Currency
    "currency": "USD",
    
    # Offset to be applied to API call. E.g. offset of 60 will return entries 60-89.
    # DO NOT AMEND HERE. Change 'start' and 'end' variables instead.
    "offset": "30",
    
    # Distance unit
    "lunit": "km",
    
    # Limit for number of entries returned by API call. Capped at 30.
    "limit": "30",
    "bookable_start": "false",
    
    # Filter by subcategory. Comment out when doing full data collection for a city.
##    "subcategory": "36",
    
    # Unique location ID for a city.
    # A city's ID can be found in the URL of any tripadvisor page for that city, in the format "g<city ID>".
    # E.g https://www.tripadvisor.com.sg/Tourism-g298302-Penang-Vacations.html, city code is 298302 for Penang.
    "location_id": "293940"
}

# Offset index to apply to API call.
# E.g using start = 5 and end = 10 will collect entries (5 * 30) = 150 to (10 * 30)-1 = 299, a total of 150 entries.
start = 0
end = 20

# File directories. Will automatically be updated during API call.
jsonDir = r'Attraction_JSONs\XYZ\Restaurants.json'
logDir =  r'Attraction_JSONs\XYZ\log.txt'

newFileFlag = False
jsonBuffer = []
tempBuffer = []

print("Destination ID:", param['location_id'])
print("Offset: %d to %d (entries %d to %d)" %(start,end,start*30,end*30-1))

input("Press Enter to continue.")
print("Requesting...")



for offset in range(start, end):

    param['offset'] = str(offset*30)

    # Make the request
    response = requests.get(URL, params = param, headers = auth)

    # Check if request was successful
    if response.status_code == 200:
        print("Request successful for offset", offset)
    else:
        print("Request %d failed with error code" % offset, response.status_code)
        sys.exit()

    # Break from loop if current data field of request is empty (no more attractions)
    # Terminate script 
    responseData = response.json()['data']
    if len(responseData) == 0:
        if len(tempBuffer) == 0:
            print("First entry is empty, terminating program.")
            sys.exit(0)
        else:
            print("End of restaurants list.")
            break
    
    # Append request payload to temporary buffer
    tempBuffer += responseData

    # Read location string from first entry for directory naming.
    if offset == start:
        if tempBuffer[0]["address_obj"]['state'] != None:
            loc = tempBuffer[0]["address_obj"]['country']+'_'+tempBuffer[0]["address_obj"]['state']
        elif tempBuffer[0]["address_obj"]['city'] != None:
            loc = tempBuffer[0]["address_obj"]['country']+'_'+tempBuffer[0]["address_obj"]['city']
        else:
            loc = tempBuffer[0]["address_obj"]['country']+'_'+tempBuffer[0]["address_obj"]['street2']
        jsonDir = 'Attraction_JSONs\\'+ loc + '\\Restaurants.json'
        logDir =  'Attraction_JSONs\\'+ loc + '\\log.txt'
    
    # Wait a bit before calling API again
    sleep(1)

# Check if destination file is empty or already exists.
# If file exists, load data into buffer and append entries, otherwise create a new file.
try:
    if os.stat(jsonDir).st_size > 0:
        print ("Restaurants.json already exists.")
        try:
            with open(jsonDir, 'r') as file:
               jsonBuffer = json.load(file)
               jsonBuffer += tempBuffer
               print("Data will be appended to existing file.")
        except:
            print("Error parsing JSON.")
            sys.exit(0)
        
    else:
        print ("File is empty, appending to file.")
        jsonBuffer = tempBuffer
except OSError:
    newFileFlag = True
    print ("File does not exist, a new file will be created.")
    jsonBuffer = tempBuffer

# Append buffer to local JSON file
os.makedirs(os.path.dirname(jsonDir), exist_ok = True)
with open(jsonDir, 'w') as file:
    json.dump(jsonBuffer, file, indent = 4, separators = (',', ': '))

# Log request to file
with open(logDir, 'a') as file:
    if newFileFlag == True:
        file.write("Restaurants.json created with offset %d to %d (entries %d to %d) at %s.\n" % (start,end,start*30,end*30-1,ctime()))
    else:
        file.write("Restaurants.json updated with offset %d to %d (entries %d to %d) at %s.\n" % (start,end,start*30,end*30-1,ctime()))

print("Operation complete.")
