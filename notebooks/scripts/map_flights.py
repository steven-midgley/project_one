import datetime
import folium
import pandas as pd

craft_categories = {
    0: {"No information at all": "gray"},
    1: {"No ADS-B Emitter Category Information": "black"},
    2: {"Light (< 15500 lbs)": "lightblue"},
    3: {"Small (15500 to 75000 lbs)": "green"},
    4: {"Large (75000 to 300000 lbs)": "orange"},
    5: {"High Vortex Large (aircraft such as B-757)": "red"},
    6: {"Heavy (> 300000 lbs)": "darkred"},
    7: {"High Performance (> 5g acceleration and 400 kts)": "purple"},
    8: {"Rotorcraft": "lightgreen"},
    9: {"Glider / sailplane": "darkgreen"},
    10: {"Lighter-than-air": "cadetblue"},
    11: {"Parachutist / Skydiver": "pink"},
    12: {"Ultralight / hang-glider / paraglider": "lightyellow"},
    13: {"Reserved": "gray"},
    14: {"Unmanned Aerial Vehicle": "lightgray"},
    15: {"Space / Trans-atmospheric vehicle": "beige"},
    16: {"Surface Vehicle – Emergency Vehicle": "red"},
    17: {"Surface Vehicle – Service Vehicle": "darkblue"},
    18: {"Point Obstacle (includes tethered balloons)": "blue"},
    19: {"Cluster Obstacle": "darkpurple"},
    20: {"Line Obstacle": "darkgray"},
}


def map_flights(df):
    # location=[39.8283, -98.5795] >> replace this with the lon lat of the origin country
    map = folium.Map(
        location=(0, 0),
        zoom_control=True,
        zoom_start=2,
        tiles=folium.TileLayer(no_wrap=True),
    )
    feature_groups = {}

    for index, row in df.iterrows():
        if pd.notna(row["longitude"]) and pd.notna(row["latitude"]):
            category = row["category"]

            if category not in craft_categories:
                description = "Unknown"
                color = "grey"
            else:
                description, color = list(craft_categories[category].items())[0]

            popup_html = call_to_action(row)

            if category not in feature_groups:
                feature_groups[category] = folium.FeatureGroup(
                    name=f"{description} ({category})"
                )

            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                tooltip=f"📞🪧: {row['callsign']}",
                popup=popup_html,
                icon=folium.Icon(icon="plane", color=color),
            ).add_to(feature_groups[category])
    for feature in feature_groups.values():
        feature.add_to(map)

    folium.LayerControl().add_to(map)
    return map._repr_html_()


def call_to_action(row):
    return f"""
            <div>
                <p><strong>Flight:</strong> {row['callsign']}</p>
                <a href='/crafy-details/{row['callsign']}'>View details</a>
            </div>
            """


# <strong>Arrival:</strong> {data['estArrivalAirport'] or "N/A"} <br/>
# <strong>Departure:</strong> {data['estDepartureAirport'] or "N/A"} <br/>
