import os
from opensky_api import OpenSkyApi
from flask import Flask, render_template, send_from_directory
from scripts.flight_path import flight_path
from scripts.opensky import get_states
from scripts.map_flights import map_flights

app = Flask(__name__)
NOTEBOOKS_DIR = os.path.join(os.getcwd(), "notebooks")


@app.route("/")
def home():
    notebook_dirs = os.listdir(NOTEBOOKS_DIR)
    notebooks = [file for file in notebook_dirs if file.endswith(".ipynb")]
    return render_template("home.html", notebooks=notebooks)


@app.route("/notebooks/<filename>")
def get_notebook(filename):
    return send_from_directory(NOTEBOOKS_DIR, filename)


@app.route("/all_crafts")
def all_crafts():
    map_html = map_flights(get_states(OpenSkyApi()))
    return render_template("index.html", map_html=map_html)


@app.route("/flight_path/<icao24>/<color>")
def craft_details(icao24, color):
    map_html = flight_path(icao24, color)
    return render_template("index.html", map_html=map_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
