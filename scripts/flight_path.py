import folium
from opensky_api import OpenSkyApi
from scripts.opensky import get_flight_details


def flight_path(icao24, color):
    api = OpenSkyApi()
    data = get_flight_details(api, icao24)

    origin_lat = data.path[0][1]
    curr_lat = data.path[len(data.path) - 1][1]
    origin_lon = data.path[0][2]
    curr_lon = data.path[len(data.path) - 1][2]
    way_points = [(p[1], p[2]) for p in data.path]

    map = folium.Map(
        location=[curr_lat, curr_lon],
        tiles=folium.TileLayer(no_wrap=True),
    )

    folium.Marker(
        location=[origin_lat, origin_lon],
        tooltip="Origin Location",
        popup="Flight Path",
        icon=folium.Icon(icon="plane", color=color),
    ).add_to(map)

    folium.Marker(
        location=[curr_lat, curr_lon],
        tooltip="Current Location",
        popup="Flight Path",
        icon=folium.Icon(icon="plane", color=color),
    ).add_to(map)

    folium.PolyLine(
        locations=way_points,
        color=color,
        weight=2.5,
        opacity=1,
    ).add_to(map)

    return map._repr_html_()
