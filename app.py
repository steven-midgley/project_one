from flask import Flask, render_template, stream_template
import folium
from notebooks.states import get_us_flights, get_craft_flights
from notebooks.scripts.add_to_maps import add_to_map
from notebooks.scripts.track_flight_icao24 import track_flight_icao24

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/all_crafts")
def all_crafts():
    us_flights = get_us_flights()
    map_html = add_to_map(us_flights)
    return render_template("index.html", map_html=map_html)


@app.route("/icao24_flight_path")
def flight_path():
    flight = get_craft_flights()
    map_html = track_flight_icao24(flight)
    return render_template("index.html", map_html=map_html)


if __name__ == "__main__":
    app.run(debug=True)
