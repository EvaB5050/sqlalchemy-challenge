# sqlalchemy-challenge
Data Bootcamp Module 10 Challenge

Congratulations! You've decided to treat yourself to a long holiday
vacation in Honolulu, Hawaii. To help with your trip planning, you
decide to do a climate analysis about the area. 

<img src="https://static.bc-edx.com/data/dla-1-2/m10/lms/surfs-up.jpg" alt="Surfs Up" width="500" height="300">


## PART 1: Analyse and Explore the Climate Data

Use SQLAlchemy ORM queries, Pandas, and Matplotlib to do a basic climate analysis and data
exploration of your climate database. 

* Use the provided files `climate_starter.ipynb` and
  `hawaii.sqlite` ) to complete your climate analysis and data exploration.

* Use the SQLAlchemy `create_engine()` function to connect to your SQLite
database.

* Use the SQLAlchemy `automap_base()` function to reflect your tables into
classes, then save references to the classes named `station` and
`measurement`.

* Link Python to the database by creating a SQLAlchemy session.

IMPORTANT: Remember to close your session at the end of your notebook.

* Perform a precipitation analysis and then a station analysis by
completing the steps in the following two subsections.

### Precipitation Analysis 
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by
querying the previous 12 months of data.
HINT: Don't pass the date as a variable to your query.

3. Select only the "date" and "prcp" values.

4. Load the query results into a Pandas DataFrame. Explicitly set the
column names.

5. Sort the DataFrame values by "date".

6. Plot the results by using the DataFrame `plot` method, as the following
image shows:


<img src="https://static.bc-edx.com/data/dla-1-2/m10/lms/img/precipitation.jpg" alt="A screenshot depicts the plot" width="440" height="310">

7. Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis 
1. Design a query to calculate the total number of
stations in the dataset.

2. Design a query to find the most-active stations (the stations
that have the most rows). 

* List the stations and observation counts in descending order.
* Which station id has the greatest number
of observations?
* Using the most-active station id, calculate the lowest, highest, and
average temperatures.
HINT: Use functions such as `func.min`, `func.max`, `func.avg` and `func.count`

3. Design a query to obtain the previous 12 months of temperature observation
(TOBS) data. 

* Filter by the station that has the greatest number of observations.
* Query the previous 12 months of TOBS data for that station.
* Plot the results as a histogram with bins=12, as the following image
shows:

<img src="https://static.bc-edx.com/data/dla-1-2/m10/lms/img/station-histogram.jpg" alt="A screenshot depicts the histogram." width="440" height="310">


4. Close your session.


## PART 2: Design Your Climate App 

Design a Flask API based on the queries developed.
Use Flask to create the following routes:

1. `/`
* Start at the homepage.
* List all the available routes.

2. `/api/v1.0/precipitation`
* Convert the query results to a dictionary by
using `date` as the key and `prcp` as the value.
* Return the JSON representation of your dictionary.

3. `/api/v1.0/stations`
*  Return a JSON list of stations from the dataset.
  
5. `/api/v1.0/tobs`
* Query the dates and temperature observations of the
most-active station for the previous year of data.
* Return a JSON list of temperature observations for the previous year.

5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
* Return a JSON list of the minimum temperature, the average temperature, and the maximum
temperature for a specified start or start-end range.

* For a specified start, calculate` TMIN`, `TAVG`, and `TMAX` for all the dates
greater than or equal to the start date.

* For a specified start date and end date, calculate `TMIN`, `TAVG`, and `TMAX`
for the dates from the start date to the end date, inclusive.

#### HINTS
* Join the station and measurement tables for some of the queries.
* Use the Flask `jsonify` function to convert your API data to a valid JSON
response object.










