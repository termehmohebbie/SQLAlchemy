# importing dependencies
from flask import Flask

# creating the app
app = Flask(__name__)

# defining the index route (Home Page)
@app.route("/")
def home():
    print("Request for Home Page!!")
    return(
        "Hello, Welcome to the Home Page!"
        "Available routes :"
        "/api/v1.0/precipitation"
        "/api/v1.0/stations"
        "/api/v1.0/tobs"
        "/api/v1.0/<start>"
        "/api/v1.0/<start>/<end>"
    )