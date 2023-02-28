# sqlalchemy-challenge
## Background
In this project we're doing a climate analysis about Honolulu, Hawaii to plan a trip!!

## Part 1: Analyze and Explore the Climate Data
In this section, we used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, we used SQLAlchemy ORM queries, Pandas, and Matplotlib.

We have a SQLite database and we're using SQLAlchemy to connect to that database and reflect the tables into classes, so that we're able to link Python to the database by creating a SQLAlchemy session.

### Precipitation Analysis
* Finding the most recent date in the dataset.

* Using that date to get the previous 12 months of precipitation data by querying the previous 12 months of data.

* Loading the query results into a Pandas DataFrame, and setting the index to the "date" column.

* Sorting the DataFrame values by "date" and plotting the results :
![y](https://user-images.githubusercontent.com/114199979/221988763-9d4d802d-f691-46bf-ae80-df3e6be10c22.jpg)

### Station Analysis
* Designing a query to calculate the total number of stations in the dataset.

* Designing a query to find the most-active stations (that is, the stations that have the most rows).

* Designing a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

* Designing a query to get the previous 12 months of temperature observation (TOBS) data and plotting the results as a histogram :


![u'](https://user-images.githubusercontent.com/114199979/221990608-9ba96232-c618-4007-b372-2a1ec227a3bc.jpg)


## Part 2: Design the Climate App
Now that we’ve completed the initial analysis, we’ll design a Flask API based on the queries that we just developed. To do so, we used Flask to create our routes as follows:

1. (/) :
* Start at the homepage.
* List all the available routes.

2. (/api/v1.0/precipitation) :
* Convert the query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
* Return the JSON representation of your dictionary.

3. (/api/v1.0/stations) :
* Return a JSON list of stations from the dataset.

4. (/api/v1.0/tobs) :
* Query the dates and temperature observations of the most-active station for the previous year of data.
* Return a JSON list of temperature observations for the previous year.

5. (/api/v1.0/<start>) and (/api/v1.0/<start>/<end>) :
* Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
* For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
* For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
