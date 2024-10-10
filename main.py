from opensky_api import OpenSkyApi
from datetime import datetime, timedelta
import pandas as pd


now = datetime.now()
last_hour = now - timedelta(minutes=60)
unix_hour = int(last_hour.timestamp())
unix_now = int(now.timestamp())


# DO MORE WITH THIS DATASET.
def get_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    list_states = []
    states = api.get_states()

    for s in states.states:
        list_states.append(
            {
                "icao24": s.icao24,
                "callsign": s.callsign,
                "origin_country": s.origin_country,
                "time_position": s.time_position,
                "last_contact": s.last_contact,
                "longitude": s.longitude,
                "latitude": s.latitude,
                "geo_altitude": s.geo_altitude,
                "on_ground": s.on_ground,
                "velocity": s.velocity,
                "true_track": s.true_track,
                "vertical_rate": s.vertical_rate,
                "sensors": s.sensors,
                "baro_altitude": s.baro_altitude,
                "squawk": s.squawk,
                "spi": s.spi,
                "position_source": s.position_source,
                "category": s.category,
            }
        )

    df = pd.DataFrame(list_states)

    df.to_csv("data/flight_states.csv", index=False)
    print("Flight states have been saved to 'flight_states.csv'.")


# get_states(OpenSkyApi())


def get_arrivals():
    """Fetch and save arrivals by airport to a CSV file."""
    api = OpenSkyApi()
    arrivals = api.get_arrivals_by_airport("EDDF", unix_hour, unix_now)
    if arrivals is None:
        print("No data received from API for arrivals.")
        return

    arrival_data = []
    for flight in arrivals:
        print(flight)
        arrival_data.append(
            {
                "icao24": flight.icao24,
                "firstSeen": flight.firstSeen,
                "estDepartureAirport": flight.estDepartureAirport,
                "lastSeen": flight.lastSeen,
                "estArrivalAirport": flight.estArrivalAirport,
                "callsign": flight.callsign,
                "estDepartureAirportHorizDistance": flight.estDepartureAirportHorizDistance,
                "estDepartureAirportVertDistance": flight.estDepartureAirportVertDistance,
                "estArrivalAirportHorizDistance": flight.estArrivalAirportHorizDistance,
                "estArrivalAirportVertDistance": flight.estArrivalAirportVertDistance,
                "departureAirportCandidatesCount": flight.departureAirportCandidatesCount,
                "arrivalAirportCandidatesCount": flight.arrivalAirportCandidatesCount,
            }
        )

    df = pd.to(arrival_data)
    df.to_csv("data/arrivals.csv", index=False)
    print("Arrivals have been saved to data/arrivals.")


# get_arrivals()


def get_departures(api, airport_code, begin, end):
    """Fetch and save departures by airport to a CSV file."""
    departures = api.get_departures_by_airport(airport_code, begin, end)

    departure_data = []
    for flight in departures:
        departure_data.append(
            {
                "icao24": flight.icao24,
                "firstSeen": flight.firstSeen,
                "estDepartureAirport": flight.estDepartureAirport,
                "lastSeen": flight.lastSeen,
                "estArrivalAirport": flight.estArrivalAirport,
                "callsign": flight.callsign,
                "estDepartureAirportHorizDistance": flight.estDepartureAirportHorizDistance,
                "estDepartureAirportVertDistance": flight.estDepartureAirportVertDistance,
                "estArrivalAirportHorizDistance": flight.estArrivalAirportHorizDistance,
                "estArrivalAirportVertDistance": flight.estArrivalAirportVertDistance,
                "departureAirportCandidatesCount": flight.departureAirportCandidatesCount,
                "arrivalAirportCandidatesCount": flight.arrivalAirportCandidatesCount,
            }
        )

    df = pd.DataFrame(departure_data)
    df.to_csv("data/departures.csv", index=False)
    print("Departures have been saved to 'departures.csv'.")


# get_departures(OpenSkyApi(), "EDDF", unix_hour, unix_now)


# EXPERIMENTAL WORK BY API SO NOT THE MOST RELIABLE SOURCE OF INFO
def get_flights(api, icao24, begin, end):
    """Fetch flights by aircraft and save to a CSV file."""
    flights = api.get_flights_by_aircraft(icao24, begin, end)

    flights_data = []
    for flight in flights:
        flights_data.append(
            {
                "icao24": flight.icao24,
                "startTime": flight.startTime,
                "endTime": flight.endTime,
                "calllsign": flight.calllsign,
                "path": flight.path,
            }
        )

    df = pd.DataFrame(flights_data)
    df.to_csv("data/flights_by_aircraft.csv", index=False)
    print("flights have been saved to 'flights_by_aircraft.csv'.")


# get_flights(OpenSkyApi(), "3c4b26", unix_hour, unix_now)
# HERE GIVE THE icao24 AND DATES IN UNIX TIMESTAMP FORMATION
