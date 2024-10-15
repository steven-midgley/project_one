import folium
from opensky_api import OpenSkyApi
from notebooks.scripts.opensky import get_flight_details


def flight_details(icao24):
    data = get_flight_details(OpenSkyApi(), icao24)
    print(data)
    poly_colors = [
        "green",
        "blue",
        "purple",
        "orange",
        "red",
        "darkgreen",
        "darkred",
        "lightblue",
        "lightgreen",
        "pink",
        "beige",
        "lightred",
        "gray",
        "black",
        "cadetblue",
        "lightgray",
        "darkblue",
        "darkpurple",
        "white",
    ]

    origin_lat = data.iloc[0].latitude
    origin_lon = data.iloc[0].longitude
    way_points = []

    map = folium.Map(
        location=[origin_lat, origin_lon],
        zoom_start=4,
        tiles=folium.TileLayer(no_wrap=True),
    )
    for index, row in data.iterrows():

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            tooltip="📝",
            popup="Flight Path",
            icon=folium.Icon(icon="plane", color=poly_colors[index % len(poly_colors)]),
        ).add_to(map)

        way_points.append([row["latitude"], row["longitude"]])

    for point in range(len(way_points) - 1):
        folium.PolyLine(
            (way_points[point], way_points[point + 1]),
            color=poly_colors[point % len(poly_colors)],
            weight=2.5,
            opacity=1,
        ).add_to(map)

    return map._repr_html_()
