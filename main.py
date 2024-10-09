from opensky_api import OpenSkyApi
import datetime
import pandas as pd


def initialize_api():
    """Initialize the OpenSky API."""
    sky_api = OpenSkyApi()
    return sky_api


# DO MORE WITH THIS DATASET.
def get_flight_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    states = api.get_states()

    flight_data = []
    for s in states.states:
        flight_data.append(
            {
                "Longitude": s.longitude,
                "Latitude": s.latitude,
                "Barometric Altitude": s.baro_altitude,
                "Velocity": s.velocity,
            }
        )

    df = pd.DataFrame(flight_data)

    df.to_csv("data/test_flight_states.csv", index=False)
    print(f"Flight states have been saved to 'flight_states.csv'.")


# api = initialize_api()
# get_flight_states(api)


def get_arrivals(api, airport_code, begin, end):
    """Fetch and save arrivals by airport to a CSV file."""
    arrivals = api.get_arrivals_by_airport(airport_code, begin, end)

    arrival_data = []
    for flight in arrivals:
        arrival_data.append(
            {
                "Arrival Airport": flight.estArrivalAirport,
                "Departure Airport": flight.estDepartureAirport,
                "Arrival Time": flight.lastSeen,
                "Time of Departure": flight.firstSeen,
            }
        )

    df = pd.DataFrame(arrival_data)
    df.to_csv("data/test_arrivals.csv", index=False)
    print(f"Arrivals have been saved to 'arrivals.csv'.")


api = initialize_api()
get_arrivals(api, "EDDF", 1672556401, 1673074801)
# HERE GIVE THE CODE FOR AIRPORT AND DATES IN UNIX TIMESTAMP FORMATION


def get_departures(api, airport_code, begin, end):
    """Fetch and save departures by airport to a CSV file."""
    departures = api.get_departures_by_airport(airport_code, begin, end)

    departure_data = []
    for flight in departures:
        departure_data.append(
            {
                "Time of Departure": flight.firstSeen,
                "Departure Airport": flight.estDepartureAirport,
                "Arrival Airport": flight.estArrivalAirport,
                "Arrival Time": flight.lastSeen,
                "Horizonal Distance From Departure": flight.estDepartureAirportHorizDistance,
                "Vertical Distance From Departure": flight.estDepartureAirportVertDistance,
                "Horizonal Distance From Arrival": flight.estArrivalAirportHorizDistance,
                "Vertical Distance From Arrival": flight.estArrivalAirportVertDistance,
            }
        )

    df = pd.DataFrame(departure_data)
    df.to_csv("departures.csv", index=False)
    print(f"Departures have been saved to 'departures.csv'.")


api = initialize_api()
# get_departures(api,"EDDF",1672556401,1673074801)
# HERE GIVE THE CODE FOR AIRPORT AND DATES IN UNIX TIMESTAMP FORMATION


# EXPEREMENTAL WORK BY API SO NOT THE MOST RELYABLE SOURCE OF INFO
def get_flights(api, icao24, begin, end):
    """Fetch flights by aircraft and save to a CSV file."""
    flights = api.get_flights_by_aircraft(icao24, begin, end)

    flights_data = []
    for flight in flights:
        flights_data.append(
            {
                "icao24": flight.icao24,
                "Time of Departure": flight.firstSeen,
                "Departure Airport": flight.estDepartureAirport,
                "Arrival Airport": flight.estArrivalAirport,
                "Arrival Time": flight.lastSeen,
                "Horizonal Distance From Departure": flight.estDepartureAirportHorizDistance,
                "Vertical Distance From Departure": flight.estDepartureAirportVertDistance,
                "Horizonal Distance From Arrival": flight.estArrivalAirportHorizDistance,
                "Vertical Distance From Arrival": flight.estArrivalAirportVertDistance,
            }
        )

    df = pd.DataFrame(flights_data)
    df.to_csv("flights_by_aircraft.csv", index=False)
    print(f"flights have been saved to 'flights_by_aircraft.csv'.")


api = initialize_api()
# get_flights(api,"3c4b26",1672556401,1673074801)
# HERE GIVE THE icao24 AND DATES IN UNIX TIMESTAMP FORMATION
