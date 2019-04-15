import pandas as pd
import json
import os

# Function, make directory for a path
def mkdir(path):
    # Check whether exist this directory
    folder = os.path.exists(path)

    # If not, create one
    if not folder:
        os.makedirs(path)

# The list for train's name, excluding 'red' line, because I will use red line directly
list = ['mattapan', 'orange', 'blue', 'greenb', 'greenc', 'greend', 'greene']

# Using Pandas to format the first json file - 'Red' line's json file
data = pd.DataFrame(json.loads(open('/Users/Eddy/Desktop/Python_MBTA/MBTA_Raw_Stop_Data/red.json', 'r+').read()))

# For all train's name in list
for train in list:

    # Read next json file in the list one by one
    next = pd.DataFrame(json.loads(open('/Users/Eddy/Desktop/Python_MBTA/MBTA_Raw_Stop_Data/' + train + '.json', 'r+').read()))

    # Try to combine the two data files
    data = pd.concat([data,next],axis=0)

# Remove the duplicated data in the file after For loop
id_location_file = data.drop_duplicates()

for i in range(3, 27, 2):

    # Read [stop id]/[time period]/[entries number] files one by one
    id_entries_file = pd.read_csv('/Users/Eddy/Desktop/Python_MBTA/Step2_time/' + str(i%24) + '_' + str((i+2)%24) + '.csv')

    # Merge the data file with stop location file
    id_entries_file = pd.merge(id_entries_file, id_location_file, on=['id'])

    mkdir('/Users/Eddy/Desktop/Python_MBTA/Step3/')

    # Write new data into files
    id_entries_file.to_csv('/Users/Eddy/Desktop/Python_MBTA/Step3/' + str(i%24) + '_' + str((i+2)%24) + '.csv', index=False)