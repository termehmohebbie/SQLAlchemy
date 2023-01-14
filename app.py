# importing dependencies
from flask import Flask

# creating the app
app = Flask(__name__)

# defining the index route (Home Page)
@app.route("/")
def home():
    print("Request for Home Page!!")
    return(
        "Hello, Welcome to the Home Page!<br/>"
        "Available routes :<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start><br/>"
        "/api/v1.0/<start>/<end><br/>"
    )

if __name__ == "__main__":
    app.run(debug=True)