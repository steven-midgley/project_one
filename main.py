from opensky_api import OpenSkyApi
import datetime
import pandas as pd


def initialize_api():
    """Initialize the OpenSky API."""
    # "hadhatter", "287a6655aa625870d39b8acb2a852d25"
    sky_api = OpenSkyApi()
    return sky_api


api = initialize_api()


# DO MORE WITH THIS DATASET.
def get_flight_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    states = api.get_states()

    flight_data = []
    for s in states.states:
        flight_data.append(
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

    df = pd.DataFrame(flight_data)

    df.to_csv("data/flight_states.csv", index=False)
    print("Flight states have been saved to 'flight_states.csv'.")


get_flight_states(api)


def get_arrivals(api, airport_code, begin, end):
    """Fetch and save arrivals by airport to a CSV file."""
    arrivals = api.get_arrivals_by_airport(airport_code, begin, end)
    print(arrivals)
    arrival_data = []
    for flight in arrivals:
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
    print("Arrivals have been saved to data/.")


get_arrivals(api, "EDDF", 1688686800, 1689291600)
# HERE GIVE THE CODE FOR AIRPORT AND DATES IN UNIX TIMESTAMP FORMATION


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


get_departures(api, "EDDF", 1688686800, 1689291600)
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
                "startTime": flight.startTime,
                "endTime": flight.endTime,
                "calllsign": flight.calllsign,
                "path": flight.path,
            }
        )

    df = pd.DataFrame(flights_data)
    df.to_csv("data/flights_by_aircraft.csv", index=False)
    print("flights have been saved to 'flights_by_aircraft.csv'.")


get_flights(api, "3c4b26", 1688686800, 1689291600)
# HERE GIVE THE icao24 AND DATES IN UNIX TIMESTAMP FORMATION
