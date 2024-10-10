from opensky_api import OpenSkyApi
import datetime
import pandas as pd


def initialize_api():
    """Initialize the OpenSky API."""
    api = OpenSkyApi("hadhatter", "287a6655aa625870d39b8acb2a852d25")
    return api


# DO MORE WITH THIS DATASET.
def get_flight_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    states = api.get_states()

    flight_data = []
    for s in states.states:
        flight_data.append(
            {
                "icao24": s.icao24,
                "lon": s.longitude,
                "lat": s.latitude,
                "baro_alt": s.baro_altitude,
                "velocity": s.velocity,
            }
        )

    df = pd.DataFrame(flight_data)

    df.to_csv("data/flight_states.csv", index=False)
    print("Flight states have been saved to 'flight_states.csv'.")


get_flight_states(initialize_api())


def get_arrivals(api, airport_code, begin, end):
    """Fetch and save arrivals by airport to a CSV file."""
    arrivals = api.get_arrivals_by_airport(airport_code, begin, end)

    arrival_data = []
    for flight in arrivals:
        arrival_data.append(
            {
                "icao24": flight.icao24,
                "arrival": flight.lastSeen,
                "destination": flight.estArrivalAirport,
                "origin": flight.estDepartureAirport,
                "departure": flight.firstSeen,
                "dist_frm_orig_h": flight.estDepartureAirportHorizDistance,
                "dist_frm_orig_v": flight.estDepartureAirportVertDistance,
                "dist_frm_dest_h": flight.estArrivalAirportHorizDistance,
                "dist_frm_dest_v": flight.estArrivalAirportVertDistance,
            }
        )

    df = pd.to(arrival_data)
    df.to_csv("data/arrivals.csv", index=False)
    print("Arrivals have been saved to data/.")


get_arrivals(initialize_api(), "EDDF", 1688686800, 1689291600)
# HERE GIVE THE CODE FOR AIRPORT AND DATES IN UNIX TIMESTAMP FORMATION


def get_departures(api, airport_code, begin, end):
    """Fetch and save departures by airport to a CSV file."""
    departures = api.get_departures_by_airport(airport_code, begin, end)

    departure_data = []
    for flight in departures:
        departure_data.append(
            {
                "icao24": flight.icao24,
                "departure": flight.firstSeen,
                "origin": flight.estDepartureAirport,
                "destination": flight.estArrivalAirport,
                "arrival": flight.lastSeen,
                "dist_frm_orig_h": flight.estDepartureAirportHorizDistance,
                "dist_frm_orig_v": flight.estDepartureAirportVertDistance,
                "dist_frm_dest_h": flight.estArrivalAirportHorizDistance,
                "dist_frm_dest_v": flight.estArrivalAirportVertDistance,
            }
        )

    df = pd.DataFrame(departure_data)
    df.to_csv("data/departures.csv", index=False)
    print("Departures have been saved to 'departures.csv'.")


get_departures(initialize_api(), "EDDF", 1688686800, 1689291600)
# HERE GIVE THE CODE FOR AIRPORT AND DATES IN UNIX TIMESTAMP FORMATION


# EXPERIMENTAL WORK BY API SO NOT THE MOST RELIABLE SOURCE OF INFO
def get_flights(api, icao24, begin, end):
    """Fetch flights by aircraft and save to a CSV file."""
    flights = api.get_flights_by_aircraft(icao24, begin, end)

    flights_data = []
    for flight in flights:
        flights_data.append(
            {
                "icao24": flight.icao24,
                "departed": flight.firstSeen,
                "origin": flight.estDepartureAirport,
                "destination": flight.estArrivalAirport,
                "arrived": flight.lastSeen,
                "dist_frm_orig_h": flight.estDepartureAirportHorizDistance,
                "dist_frm_orig_v": flight.estDepartureAirportVertDistance,
                "dist_frm_dest_h": flight.estArrivalAirportHorizDistance,
                "dist_frm_dest_v": flight.estArrivalAirportVertDistance,
            }
        )

    df = pd.DataFrame(flights_data)
    df.to_csv("data/flights_by_aircraft.csv", index=False)
    print("flights have been saved to 'flights_by_aircraft.csv'.")


get_flights(initialize_api(), "3c4b26", 1688686800, 1689291600)
# HERE GIVE THE icao24 AND DATES IN UNIX TIMESTAMP FORMATION
