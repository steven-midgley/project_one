from opensky_api import OpenSkyApi
from flask import Flask, render_template
from notebooks.states import get_flights, get_flight_details
from notebooks.scripts.opensky import get_states
from notebooks.scripts.map_flights import map_flights
from notebooks.scripts.flight_details import flight_details

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/all_crafts")
def all_crafts():
    get_states(OpenSkyApi())
    flights = get_flights()
    map_html = map_flights(flights)
    return render_template("index.html", map_html=map_html)


@app.route("/crafy-details/<callsign>")
def craft_details(callsign):
    print(callsign)
    flight = get_flight_details(callsign)
    map_html = flight_details(flight)
    return render_template("index.html", map_html=map_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
