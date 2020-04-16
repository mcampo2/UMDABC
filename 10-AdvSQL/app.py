from flask import Flask
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

app = Flask(__name__)

# Create engine for climate data
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
session = Session(engine)
inspector = inspect(engine)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
#print(inspector.get_table_names())

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# print column names
# print(Measurement.__table__.columns)
# print(Station.__table__.columns)


# Create our session (link) from Python to the DB
session = Session(engine)

# print tables and table columns
#for table in Base.classes:
#    print(table.__table__)
#    print("-" * 15)
#    [print(x) for x in table.__dict__ if not x.startswith("_")]
#    print()

precipitation_json = {}
for row in session.query(Measurement).all():
    precipitation_json[row.date]  = row.prcp

stations_json = {}
for row in session.query(Station).all():
    stations_json[row.station] = row.name

# get 1-year from last measurement
min_date = session.query(func.min(Measurement.date)).first()[0]
max_date = session.query(func.max(Measurement.date)).first()[0]
end_date = dt.datetime.strptime(max_date, "%Y-%m-%d")
start_date = end_date - dt.timedelta(days=365)

tobs_json = {}
for row in session.query(Measurement).filter(Measurement.date >= start_date).all():
    tobs_json[row.date] = row.tobs

@app.route("/")
def home():
    # List all routes that are available.
    print("Serving homepage")
    return "Available Routes:</br>"  + \
        "<a href=\"api/v1.0/precipitation\">/api/v1.0/precipitation</a></br>" + \
        "<a href=\"api/v1.0/stations\">/api/v1.0/stations</a></br>" + \
        "<a href=\"api/v1.0/tobs\">/api/v1.0/tobs</a></br>" + \
        "<a href=\"api/v1.0/" + min_date + "\">/api/v1.0/&lt;start&gt;</a></br>" + \
        "<a href=\"api/v1.0/" + min_date + "/" + max_date + "\">/api/v1.0/&lt;start&gt;/&lt;end&gt;</a>"

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Return a Dictionary using date as the key and prcp as the value.
    return precipitation_json

@app.route("/api/v1.0/stations")
def stations():
    # Return a JSON list of stations from the dataset.
    return stations_json

@app.route("/api/v1.0/tobs")
def tobs():
    # query for the dates and temperature observations from a year from the last data point.
    # Return a JSON list of Temperature Observations (tobs) for the previous year.
    return tobs_json

@app.route("/api/v1.0/<start>")
def start(start):
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    session = Session(create_engine("sqlite:///Resources/hawaii.sqlite"))
    tmin = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).first()[0]
    tavg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).first()[0]
    tmax = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).first()[0]
    session.close()
    return {"TMIN": tmin, "TAVG": tavg, "TMAX": tmax}

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    session = Session(create_engine("sqlite:///Resources/hawaii.sqlite"))
    tmin = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).first()[0]
    tavg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).first()[0]
    tmax = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).first()[0]
    session.close()
    return {"TMIN": tmin, "TAVG": tavg, "TMAX": tmax}

if __name__ == "__main__":
    app.run()