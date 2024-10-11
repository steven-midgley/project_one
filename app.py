from flask import Flask, render_template
import folium

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all_crafts")
def all_crafts():
    return render_template("all_crafts.html")


@app.route("/icao24_flight_path")
def flight_path():
    return render_template("icao24_flight_path.html")


if __name__ == "__main__":
    app.run(debug=True)
