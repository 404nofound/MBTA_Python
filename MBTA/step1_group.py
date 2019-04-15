import pandas as pd
import numpy as np
import os

# Function, divided all data into groups by time period, like [1AM-3AM; 3AM-5Am ...]
def binning(column, points, labels=None, month=0, stop=0):

    '''
    Notes: The Row Data from MBTA webiste
           The Time format is from 3:00 to 27:00, means 3:00 AM today to next day 3:00 AM
           And in the csv file, it use int to replace date format, like 300 means 3:00 AM; 1500 means 3:00 PM

    :param column: use which column to divide, here we use TIME_PERIOD column
    :param points: the break points we use to divide
    :param labels: the labels for result groups that have been divided
    :param month: used to record error
    :param stop: used to record error
    '''

    # Get max time and min time from data
    minval = column.min()
    maxval = column.max()

    # Handle break points and labels errors and print
    while maxval <= points[len(points)-1]:
        print ('Month: ' + str(month) + ' Stop: ' + stop)
        del points[len(points)-1]
        del labels[len(points)-1]

    while minval >= points[0]:
        print ('Month: ' + str(month) + ' Stop: ' + stop)
        del points[0]
        del labels[0]

    # The full break points includes min, max time
    break_points = [minval] + points + [maxval]

    # If user doesn't provide labels, using int number to replace, here I have provided labels, so it doesn't work
    if not labels:
        labels = range(len(points)+1)

    # cut() function to divide data into groups and return them
    columnbin = pd.cut(column, bins=break_points, labels=labels, include_lowest=True)

    return columnbin

# Function, make directory. if exist, do nothing
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)

# Using Pandas read every months' row data, from January to July, there only 7 months provide by MBTA this year until now
for month in range(1,8):
    csvfile = pd.read_csv('/Users/Eddy/Desktop/Python_MBTA/MBTA_Raw_Entry_Data/2018_0' + str(month) + '.csv')

    # Format file to prepare data analysis
    df = pd.DataFrame(csvfile)

    # Divide data into different part group by stop id
    grouped = df.groupby('GTFS_STOP_ID', as_index=False)

    # For every stop's data, using binning() function to divide into different time period
    for stop, group in grouped:

        # Define break points
        points = [500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500]

        # Define labels
        labels = ['3AM-5AM', '5AM-7AM', '7AM-9AM', '9AM-11AM', '11AM-1PM', '1PM-3PM', '3PM-5PM', '5PM-7PM', '7PM-9PM',
                  '9PM-11PM', '11PM-1AM', '1AM-3AM']

        # Create new column [TIME_PERIOD_Bin] for the result returned by binning() function
        group['TIME_PERIOD_Bin'] = binning(group['TIME_PERIOD'], points, labels, month, stop)

        # Format all the data again
        df_station = pd.DataFrame(group)

        # Until now, all data have been grouped by stop_id, and then grouped by time period that we create
        group_time = df_station.groupby('TIME_PERIOD_Bin')

        # Make directory to store new csv files
        mkdir('/Users/Eddy/Desktop/Python_MBTA/Step1/' + str(month))

        # Calculate the sum of entry people number for every stops and every periods
        data1 = pd.DataFrame(group_time['STATION_ENTRIES'].agg(np.sum))

        # Write into the csv files
        data1.to_csv('/Users/Eddy/Desktop/Python_MBTA/Step1/' + str(month) + "/" + stop + '.csv')