# MBTA - Python

Drawing the heat map for train stations during 24 hours. In this project, we only cover the Red, Orange, Blue, Mattapan, Green B, Green C, Green D, Green E lines.

### The Heatmap for Boston Train Stations

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/1.png">

### UML Sequence Diagram (For whole project)

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/2.png"/>

### Goals & Functions
* Show every train station on the map.
* Draw the heat points for every station.
* All heat points will combine and form the heat map.
* Generating heat map for different time period.

### Data
* There are 7 months’ (2018), about 160,000 pieces for each month, data available on MBTA website.
* Every piece of data includes Station Name, Station Id, Date, Time and People Number.
* All stations’ location data (latitude, longitude), used to show station on map (lat/log).
 
<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/3.png"/>
 
### Approach & Details
Step 1: Categorize for Every Station Every Month
>>1.	Using Pandas Library – Based on NumPy.
>>2.	Divide all data by stations.
>>3.	Divide data by time period (Every 2 hour).
>>4.	Count the entry people number for same station and same time period.

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/4.png"/>

Step 2: Change Basic Category
>>1.	Change Stop Category into Time Period Category.
>>2.	This way can make sure the heat map can work for different time periods.

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/5.png"/>

Step 3: Station Location Data (Lat / Log)
>>1.	Download station location data from MBTA API.
>>2.	Using Python to convert JSON data into CSV file.

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/6.png"/>

Step 4: Combine Location and Entry Number File
>>1.	Get Entry Number files’ station id.
>>2.  Use this id to search location file to find this id’s latitude and longitude.
>>3.  Add columns in Entry Number files automatically.
 
<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/7.png"/>

Step 5: Generate Heat Map for Every Time Period
>>1.  Use Folium Plugins to call leaflet heat map function to generate html files.
