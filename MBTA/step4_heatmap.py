from folium.plugins import HeatMap
import pandas as pd
import folium
import os

# Function, make directory for a path
def mkdir(path):
    # Check whether exist this directory
    folder = os.path.exists(path)

    # If not, create one
    if not folder:
        os.makedirs(path)

# For loop to read every analyzed data files (Including stop lat/log, and counts for draw heat map)
for i in range(3, 27, 2):

    # Define a list to store data from files
    data = []

    # Read the raw csv file's data
    file = pd.read_csv('/Users/Eddy/Desktop/Python_MBTA/Step3/' + str(i%24) + '_' + str((i+2)%24) + '.csv')

    # lat: latitude of stop location
    lat = file['lat']

    # log: longitude of stop location
    log = file['log']

    # n: entries people number for this stop (All 7 months' summary)
    n = file['n']

    # For loop to merge
    for j in range(len(lat)):

        # Child list to store object[lat,log,count]
        child = []

        # Add object into child list
        child.append(lat[j])
        child.append(log[j])
        child.append(n[j]/2100)

        # Add child list into total data list
        data.append(child)

    # Folium itself function to define a map with a view lat/log and map zoom level
    m = folium.Map([42.3, -71.1], tiles='stamentoner', zoom_start=11)

    # Add all the point data into map function
    HeatMap(data).add_to(m)

    mkdir('/Users/Eddy/Desktop/Python_MBTA/Step4_heatmap/')

    # Save the created map into a html file
    m.save('/Users/Eddy/Desktop/Python_MBTA/Step4_heatmap/heatmap' + str(i%24) + '_' + str((i+2)%24) + '.html')
