import os
import time
from opensky_api import OpenSkyApi
from datetime import datetime, timedelta, timezone
import pandas as pd


# DO MORE WITH THIS DATASET.
def get_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    states = api.get_states()

    if not states:
        print(f"states data: {states}")
        return

    states_data = []
    for s in states.states:
        states_data.append(
            {
                "icao24": s.icao24,
                "callsign": s.callsign,
                "origin_country": s.origin_country,
                "time_position": s.time_position,
                "last_contact": s.last_contact,
                "last_contact_utc": datetime.fromtimestamp(
                    s.last_contact, tz=timezone.utc
                ),
                "longitude": s.longitude,
                "latitude": s.latitude,
                "geo_altitude": s.geo_altitude,
                "on_ground": s.on_ground,
                "velocity": s.velocity,
                "true_track": s.true_track,
                "vertical_rate": s.vertical_rate,
                "baro_altitude": s.baro_altitude,
                "squawk": s.squawk,
                "category": s.category,
            }
        )

    df = pd.DataFrame(states_data)

    df.to_csv("data/flight_states.csv", mode="w", header=True, index=False)
    print()

    pass


def get_arrivals(api, airport, begin, end):
    """Fetch and save arrivals by airport to a CSV file."""
    arrivals = api.get_arrivals_by_airport(airport, begin, end)

    if arrivals is None:
        return print(f"arrival data: {arrivals}")

    arrival_data = []
    for flight in arrivals:
        print(flight)
        arrival_data.append(
            {
                "icao24": flight.icao24,
                "firstSeen": flight.firstSeen,
                "firstSeen_utc": datetime.fromtimestamp(
                    flight.firstSeen, tz=timezone.utc
                ),
                "estDepartureAirport": flight.estDepartureAirport,
                "lastSeen": flight.lastSeen,
                "lastSeen_uts": datetime.fromtimestamp(
                    flight.lastSeen, tz=timezone.utc
                ),
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

    df = pd.DataFrame(arrival_data)

    save_to_csv(df, "data/arrivals.csv")

    pass


def get_departures(api, airport, begin, end):
    """Fetch and save departures by airport to a CSV file."""
    departures = api.get_departures_by_airport(airport, begin, end)

    if departures is None:
        return print(f"departures data: {departures}")

    departure_data = []
    for flight in departures:
        departure_data.append(
            {
                "icao24": flight.icao24,
                "firstSeen": flight.firstSeen,
                "firstSeen_utc": datetime.fromtimestamp(
                    flight.firstSeen, tz=timezone.utc
                ),
                "estDepartureAirport": flight.estDepartureAirport,
                "lastSeen": flight.lastSeen,
                "lastSeen_uts": datetime.fromtimestamp(
                    flight.lastSeen, tz=timezone.utc
                ),
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

    save_to_csv(df, "data/departures.csv")

    pass


# EXPERIMENTAL WORK BY API SO NOT THE MOST RELIABLE SOURCE OF INFO
def get_flights_by_aircraft(api, icao24, begin, end):
    """Fetch flights by aircraft and save to a CSV file."""
    flights = api.get_flights_by_aircraft(icao24, begin, end)

    if flights is None:
        print(f"aircraft data: {flights}")
        return

    flights_data = []
    for flight in flights:
        flights_data.append(
            {
                "icao24": flight.icao24,
                "firstSeen": flight.firstSeen,
                "firstSeen_utc": datetime.fromtimestamp(
                    flight.firstSeen, tz=timezone.utc
                ),
                "estDepartureAirport": flight.estDepartureAirport,
                "lastSeen": flight.lastSeen,
                "lastSeen_uts": datetime.fromtimestamp(
                    flight.lastSeen, tz=timezone.utc
                ),
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

    df = pd.DataFrame(flights_data)

    save_to_csv(df, "data/flights_by_aircraft.csv")

    pass


def get_flight_interval(api, begin, end):
    interval = api.get_flights_from_interval(begin, end)

    if not interval:
        return print(f"interval data: {interval}")

    intervals = []
    for inte in interval:
        intervals.append(
            {
                "arrivalAirportCandidatesCount": inte.arrivalAirportCandidatesCount,
                "callsign": inte.callsign,
                "departureAirportCandidatesCount": inte.departureAirportCandidatesCount,
                "estArrivalAirport": inte.estArrivalAirport,
                "estArrivalAirportHorizDistance": inte.estArrivalAirportHorizDistance,
                "estArrivalAirportVertDistance": inte.estArrivalAirportVertDistance,
                "estDepartureAirport": inte.estDepartureAirport,
                "estDepartureAirportHorizDistance": inte.estDepartureAirportHorizDistance,
                "estDepartureAirportVertDistance": inte.estDepartureAirportVertDistance,
                "firstSeen": inte.firstSeen,
                "firstSeen_utc": datetime.fromtimestamp(
                    inte.firstSeen, tz=timezone.utc
                ),
                "icao24": inte.icao24,
                "lastSeen": inte.lastSeen,
                "lastSeen_utc": datetime.fromtimestamp(inte.lastSeen, tz=timezone.utc),
            }
        )

    df = pd.DataFrame(intervals)

    save_to_csv(df, "data/flights_by_interval.csv")

    pass


def save_to_csv(df, file_path):
    """Append or create a CSV file based on existence."""
    if not os.path.isfile(file_path):
        df.to_csv(file_path, mode="w", header=True, index=False)
        print(f"Created: {file_path}")
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)
        print(f"Saved: {file_path}")


if __name__ == "__main__":
    now = datetime.now()
    last_hour = now - timedelta(minutes=60)
    unix_hour = int(last_hour.timestamp())
    unix_now = int(now.timestamp())
    api = OpenSkyApi()
    airports = [
        "KATL",
        "KSLC",
        "KDFW",
        "KDEN",
        "KORD",
        "OMDB",
        "ESSA",
        "LIMC",
        "LIAU",
        "EPKK",
        "WSAC",
        "YSBK",
        "YMYB",
        "YMEN",
        "YKEL",
        "YNHS",
        "YMAV",
        "YPJI",
        "VECC",
        "KS03",
        "KABQ",
    ]
    crafts = [
        "80162c",
        "4b1818",
        "aa3cbe",
        "80162a",
        "801638",
        "3d10af",
        "88044a",
        "7c6b2f",
        "aa56da",
        "7c6b2d",
        "88044d",
        "407a38",
        "7c6b41",
        "7c6b40",
        "a3b87f",
        "8a02ff",
        "880454",
        "880452",
        "80162f",
        "880458",
        "880457",
    ]

    get_states(api)
    get_flight_interval(api, unix_hour, unix_now)
    for cr in crafts:
        get_flights_by_aircraft(api, cr, unix_hour, unix_now)
        time.sleep(1)
    for ap in airports:
        get_arrivals(api, ap, unix_hour, unix_now)
        time.sleep(1)
    for ap in airports:
        get_departures(api, ap, unix_hour, unix_now)
        time.sleep(1)
# HERE GIVE THE icao24 AND DATES IN UNIX TIMESTAMP FORMATION
