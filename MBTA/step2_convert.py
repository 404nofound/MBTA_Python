import pandas as pd
import os

class file:
    def __init__(self, path):
        self.path = path

    # Function, make directory for a path
    def mkdir(self):
        # Check whether exist this directory
        folder = os.path.exists(self.path)

        # If not, create one
        if not folder:
            os.makedirs(self.path)

    # Function, list all files' name under a special folder
    def listdir(self, list_name):
        for file in os.listdir(self.path):
            # Specially, at here, we want to remove '.csv' to get the file name
            list_name.append(file[:-4])

def main():
    # Declare a list to store file names
    name_list = []

    # Search all file names and store into name_list
    list = file('/Users/Eddy/Desktop/Python_MBTA/Step1/2/')
    list.listdir(name_list)

    # For evert name in name_list
    for name in name_list:

        # Using Pandas to read this csv file (Specially for January's data)
        csvfile = pd.read_csv('/Users/Eddy/Desktop/Python_MBTA/Step1/1/' + name + '.csv')

        # Read February to July's files
        for i in range(2, 8):
            nextcsvfile = pd.read_csv('/Users/Eddy/Desktop/Python_MBTA/Step1/' + str(i) + '/' + name + '.csv')

            # Merge the January's data file with February to July's data files
            csvfile = csvfile.join(nextcsvfile, rsuffix=i, how='outer')

            # Format final data file
            df = pd.DataFrame(csvfile)

            # Add entries people number together
            df['STATION_ENTRIES'] = df['STATION_ENTRIES'] + df['STATION_ENTRIES' + str(i)]

            # delete useless column in the csv file
            del df['TIME_PERIOD_Bin' + str(i)]
            del df['STATION_ENTRIES' + str(i)]

            # Make folder
            mkfile = file('/Users/Eddy/Desktop/Python_MBTA/Step2_stop/')
            mkfile.mkdir()

            # Write data into csv files
            df.to_csv('/Users/Eddy/Desktop/Python_MBTA/Step2_stop/' + name + '.csv')

    # Create csv file based on time period (Like: 3AM - 5AM; ...), and write into header title
    for i in range(3, 27, 2):
        mk2 = file('/Users/Eddy/Desktop/Python_MBTA/Step2_time/')
        mk2.mkdir()

        init = []
        init.insert(0, {'id', 'n'})

        init_df = pd.DataFrame(init)
        init_df.to_csv('/Users/Eddy/Desktop/Python_MBTA/Step2_time/' + str(i % 24) + '_' + str((i + 2) % 24) + '.csv',
                       header=False, index=False)

    for name in name_list:
        csv_total_file = pd.read_csv('/Users/Eddy/Desktop/Python_MBTA/Step2_stop/' + name + '.csv')

        # Index used to locate csv files' line (time period)
        index = 0

        for i in range(3, 27, 2):
            data = []

            # Number is the entries people number at a special time period
            number = csv_total_file.loc[index][2]

            # Increase the index by 1 every time
            index += 1

            # The following code is used to insert a piece of data into origin csv files
            data.insert(0, {'STATION_NAME': name, 'STATION_NUMBER': number})
            df = pd.DataFrame(data)

            # Append data into csv file
            df.to_csv('/Users/Eddy/Desktop/Python_MBTA/Step2_time/' + str(i % 24) + '_' + str((i + 2) % 24) + '.csv',
                      mode='a', header=False, index=False)

if __name__ == '__main__':
    main()