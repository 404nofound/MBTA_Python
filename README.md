# MBTA - Python

Drawing the heat map for train stations during 24 hours. In this project, we only cover the `Red, Orange, Blue, Mattapan, Green B, Green C, Green D, Green E` lines.

**Demo can be found [Here](http://3.21.206.219/python/).**

## The Heatmap for Boston Train Stations

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/1.png">

<img src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/8.png">

## UML Sequence Diagram (For whole project)

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/2.png"/>

## Goals & Functions
* Show every train station on the map.
* Draw the heat points for every station.
* All heat points will combine and form the heat map.
* Generating heat map for different time period.

## Data
* There are 7 months’ (2018), about 160,000 pieces for each month, data available on MBTA website.
* Every piece of data includes Station Name, Station Id, Date, Time and People Number.
* All stations’ location data (latitude, longitude), used to show station on map (lat/log).
 
<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/3.png"/>
 
## Approach & Details
Step 1: Categorize for Every Station Every Month
* Using Pandas Library – Based on NumPy.
* Divide all data by stations.
* Divide data by time period (Every 2 hour).
* Count the entry people number for same station and same time period.

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/4.png"/>

Step 2: Change Basic Category
* Change Stop Category into Time Period Category.
* This way can make sure the heat map can work for different time periods.

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/5.png"/>

Step 3: Station Location Data (Lat / Log)
* Download station location data from MBTA API.
* Using Python to convert JSON data into CSV file.

<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/6.png"/>

Step 4: Combine Location and Entry Number File
* Get Entry Number files’ station id.
* Use this id to search location file to find this id’s latitude and longitude.
* Add columns in Entry Number files automatically.
 
<img width="80%" height="80%" src="https://github.com/404nofound/Resource/blob/master/Images/MBTA_Python/7.png"/>

Step 5: Generate Heat Map for Every Time Period
* Use Folium Plugins to call leaflet heat map function to generate html files.
