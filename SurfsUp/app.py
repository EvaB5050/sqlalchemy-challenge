import numpy as np
import datetime as dt
from datetime import timedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#===============================================#
# Database Setup
#===============================================#

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#===============================================#
# Flask Setup
#===============================================#

app = Flask(__name__)

#===============================================#
# Flask Routes
#===============================================#

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/startdate<br/>"
        f"/api/v1.0/startdate/enddate"     
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create session from Python to the DB
    session = Session(engine)

    """Return a list of dates and precipitation (prcp) data"""
    
    # Query all dates and precipitation
    prcp_result = session.query(Measurement.prcp, Measurement.date).all()

    session.close()

    # Convert query results to a dictionary by using 'date' as the key and 'prcp' as the value
    # Return the JSON representation of the dictionary.
    
    precip_query = []
    for prcp, date in prcp_result:
        precip_dict = {}
        precip_dict["precipitation"] = prcp
        precip_dict["date"] = date
        precip_query.append(precip_dict)

    return jsonify(precip_query) 


@app.route("/api/v1.0/stations")
def stations(): 

    session = Session(engine)

    """Return a list of stations from the database""" 
    station_result = session.query(Station.station,Station.name).all()

    session.close()  
    
    stations_list = []
    for station, name in station_result:
        stations_list_dict = {}
        stations_list_dict['station'] = station
        stations_list_dict['name'] = name
        stations_list.append(stations_list_dict)
    return jsonify (stations_list) 

# Query the dates and temperature observations of the most active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
 
    session = Session(engine)

    # Query last date in database from Measurements
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    query_date = (dt.datetime.strptime(latest_date[0], "%Y-%m-%d") - dt.timedelta(days=365)).strftime('%Y-%m-%d')

    # Find the most active station in database
    active_station = session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()

    """Return a list of dates and temperature of the most active station for the last year"""
    # Query the dates and temperature observations of the most active station for the last year of data 
    results = session.query(Measurement.tobs).filter(Measurement.date >= query_date).\
filter(Measurement.station == active_station[0]).all()

    session.close()

    # Convert list of tuples into normal list
    most_active_station = list(np.ravel(results))

    return jsonify(most_active_station)

# For a specified start, calculate the minimum, average, and maximum temperature observed for all dates 
# greater than or equal to the start date entered by a user

@app.route("/api/v1.0/<start>")
# Define function, set "start" date entered by user as parameter for start_date decorator 
def start_date(start):
    session = Session(engine) 

    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""

    # Query minimum, average, and max tobs where query date is greater than or equal to the date the user enters in URL
    start_date_results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close() 

    start_date_values =[]
    for min, avg, max in start_date_results:
        start_date_dict = {}
        start_date_dict["min"] = min
        start_date_dict["average"] = avg
        start_date_dict["max"] = max
        start_date_values.append(start_date_dict)
    
    return jsonify(start_date_values)

# For a specified start date and end date, calculate the minimum, average, and maximum temperature observed 
# from the start date to the end date, inclusive

@app.route("/api/v1.0/<start>/<end>")

# Define function, set start and end dates entered by user as parameters for start_end_date decorator
def Start_end_date(start, end):
    session = Session(engine)

    """Return a list of min, avg and max tobs between start and end dates entered"""
    
    # Create query for minimum, average, and max tobs where query date is greater than or equal to the start date and less than or equal to end date user submits in URL

    start_end_date_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    session.close()
  
    # Create a list of min,max,and average temps that will be appended with dictionary values for min, max, and avg tobs queried above
    start_end_date_values = []
    for min, avg, max in start_end_date_results:
        start_end_date_dict = {}
        start_end_date_dict["min_temp"] = min
        start_end_date_dict["avg_temp"] = avg
        start_end_date_dict["max_temp"] = max
        start_end_date_values.append(start_end_date_dict) 
    

    return jsonify(start_end_date_values)
   
if __name__ == '__main__':
    app.run(debug=True)   

