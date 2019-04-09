"""

A Flask app that displays a simple Time Table 

"""

#Importing modules.
import os
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

#Setting up the database with SQLAlchemy.
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

#Creating a new flask app.
app = Flask(__name__)

#Index
@app.route("/", methods=["GET"])
"""
Index route:
    Shows a Select option to choose the day of the week.
    And a submit button.
    Submit Button sends a POST request to /tt with the option selected.

"""
def index():
    return render_template("index.html")

@app.route("/tt", methods=["POST", "GET"])
"""
Time Table route:
    Accepts both GET and POST requests.
    Gets all the periods from the database and returns to tt.html(For POST)
    Displays the index page(For GET)

"""
def tt():
    
    #For GET request
    if request.method == "GET":
        #Returning index.html if GET request.
        return render_template("index.html")

    #For POST request.
    
    #Getting the form from index.html
    name = request.form.get("name")

    #Getting the periods from the database.
    periods = db.execute(f"SELECT {name} FROM it4").fetchall()

    #SQL Query returns with () and '' around the periods.
    #Stripping ()'' off the periods.
    strpd_periods = []
    for period in periods:
        strpd_periods.append(str(period).strip("()',"))
    

    #Dictionary with abbreviations.
    #Used here the return the full name of the day.
    days_abbr = {
        'mon': 'Monday',
        'tue': 'Tuesday',
        'wed': 'Wednesday',
        'thu': 'Thursday',
        'fri': 'Friday',
        'sat': 'Saturday'
        }
    
    #Returning tt.html with periods and day as parameters.
    return render_template("tt.html", periods=strpd_periods, day=days_abbr[name])

#API
@app.route("/api/<string:day>")
"""
An API which returns the Time Table provided a day.
Only the first three letters of the day have to be specified.
For Monday:
    /api/mon
and vice versa.

"""
def api(day):
    #List of days on which classes are held.
    days_active = ['mon','tue','wed','thu','fri','sat']
    #Checking if there are classes on the specified day.
    if day in days_active:
        #Getting classes from the database.
        periods = db.execute(f"SELECT {day} FROM it4").fetchall()

        #Stripping ()', off the result from the query.
        strpd_periods = []
        for period in periods:
            strpd_periods.append(str(period).strip("()',"))

        #Returning a JSON objects with a list of classes for the specified day.
        return jsonify(periods=strpd_periods)

    else:
        #If the day format is invalid Returning an error message.
        return jsonify(error="Invalid Day.")

if __name__ == "__main__":
    app.run()
    