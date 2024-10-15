import os
import time
from opensky_api import OpenSkyApi
from datetime import datetime, timedelta, timezone
import pandas as pd

from scripts.map_flights import map_flights


def welcome_map():
    api = OpenSkyApi()
    current_flight = api.get_states()
    df = pd.DataFrame(current_flight)
    map_flights(df)
    return current_flight
