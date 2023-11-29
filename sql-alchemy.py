import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurements = Base.classes.measurements

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start_end<br/>"
    )
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # INPUT????

    # Close the session
    session.close()
#################################################
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # INPUT????

    # Close the session
    session.close()
#################################################
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # INPUT????

    # Close the session
    session.close()
#################################################
@app.route("/api/v1.0/start")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # INPUT????

    # Close the session
    session.close()
#################################################
@app.route("/api/v1.0/start_end")
def start_end():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # INPUT????

    # Close the session
    session.close()
#################################################
if __name__ == '__main__':
    app.run(debug=True)