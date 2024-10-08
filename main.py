from opensky_api import OpenSkyApi
import datetime
import pandas as pd 

def initialize_api():
    """Initialize the OpenSky API."""
    sky_api = OpenSkyApi()
    return sky_api

def get_flight_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    states = api.get_states()
    
    flight_data = []
    for s in states.states:
        flight_data.append({
            'Longitude': s.longitude,
            'Latitude': s.latitude,
            'Barometric Altitude': s.baro_altitude,
            'Velocity': s.velocity
        })
    
    df = pd.DataFrame(flight_data)
    
    df.to_csv('flight_states.csv', index=False)
    print(f"Flight states have been saved to 'flight_states.csv'.")

api = initialize_api()
get_flight_states(api)


def get_arrivals(api, airport_code, begin, end):
    """Fetch and save arrivals by airport to a CSV file."""
    arrivals = api.get_arrivals_by_airport(airport_code, begin, end)
    
    
    arrival_data = []
    for flight in arrivals:
        arrival_data.append({
            'Time of Departure':flight.firstSeen,
            'Departure Airport':flight.estDepartureAirport,
            'Arrival Airport': flight.estArrivalAirport,
            'Arrival Time': flight.lastSeen
        })

    df = pd.DataFrame(arrival_data)
    df.to_csv('arrivals.csv', index=False)
    print(f"Arrivals have been saved to 'arrivals.csv'.")
api = initialize_api()
get_arrivals(api,"EDDF",1672556401,1673074801) 

# 1704049199