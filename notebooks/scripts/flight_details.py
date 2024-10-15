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

    origin_lat = data.path[0][1]
    origin_lon = data.path[0][2]
    way_points = [(p[1], p[2]) for p in data.path]

    map = folium.Map(
        location=[origin_lat, origin_lon],
        zoom_start=4,
        tiles=folium.TileLayer(no_wrap=True),
    )

    folium.Marker(
        location=[origin_lat, origin_lon],
        tooltip="📝",
        popup="Flight Path",
        icon=folium.Icon(
            icon="plane", color=poly_colors[way_points % len(poly_colors)]
        ),
    ).add_to(map)

    folium.PolyLine(
        locations=way_points,
        color=poly_colors[way_points % len(poly_colors)],
        weight=2.5,
        opacity=1,
    ).add_to(map)

    return map._repr_html_()
