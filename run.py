import os

from flask import Flask, render_template, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv("DATABASE_TIMETABLE")
# db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/tt", methods=["POST", "GET"])
def tt():
    if request.method == "GET":
        return render_template("index.html")
    name = request.form.get("name")
    periods = db.execute(f"SELECT {name} FROM it4").fetchall()
    strpd_periods = []
    days_abbr = {
        'mon': 'Monday',
        'tue': 'Tuesday',
        'wed': 'Wednesday',
        'thu': 'Thursday',
        'fri': 'Friday',
        'sat': 'Saturday'
        }
    for period in periods:
        strpd_periods.append(str(period).strip("()',"))
    return render_template("tt.html", periods=strpd_periods, day=days_abbr[name])

@app.route("/api/<string:day>")
def api(day):
    days_active = ['mon','tue','wed','thu','fri','sat']
    if day in days_active:
        periods = db.execute(f"SELECT {day} FROM it4").fetchall()
        strpd_periods = []
        for period in periods:
            strpd_periods.append(str(period).strip("()',"))
        return jsonify(periods=strpd_periods)
    else:
        return jsonify(error="Invalid Day.")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    