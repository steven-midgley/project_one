from opensky_api import OpenSkyApi
from datetime import datetime, timedelta
import pandas as pd
import random


# DO MORE WITH THIS DATASET.
def get_states(api):
    """Fetch and save the current states of all flights to a CSV file."""
    states = api.get_states()

    if not states:
        print(f"Returned None from states: {states}")
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

    df = pd.DataFrame(states_data)

    df.to_csv(
        "data/flight_states.csv",
        mode="a",
        header=False,
        index=False,
    )
    print("Flight states have been saved to 'data/flight_states.csv'.")
    pass


def get_arrivals(api, airport, begin, end):
    """Fetch and save arrivals by airport to a CSV file."""
    arrivals = api.get_arrivals_by_airport(airport, begin, end)

    if arrivals is None:
        return print(f"Unable to get arrival data: {arrivals}")

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
    df.to_csv(
        "data/arrivals.csv",
        mode="a",
        header=False,
        index=False,
    )
    print("Arrivals have been saved to data/arrivals.csv")
    pass


def get_departures(api, airport, begin, end):
    """Fetch and save departures by airport to a CSV file."""
    departures = api.get_departures_by_airport(airport, begin, end)

    if departures is None:
        return print(f"Returned None from departures: {departures}")

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
    df.to_csv(
        "data/departures.csv",
        mode="a",
        header=False,
        index=False,
    )
    print("Departures have been saved to 'data/departures.csv'.")
    pass


# EXPERIMENTAL WORK BY API SO NOT THE MOST RELIABLE SOURCE OF INFO
def get_flights_by_aircraft(api, icao24, begin, end):
    """Fetch flights by aircraft and save to a CSV file."""
    flights = api.get_flights_by_aircraft(icao24, begin, end)

    if flights is None:
        print("Returned None from flights: {flights}")
        return

    flights_data = []
    for flight in flights:
        flights_data.append(
            {
                "icao24": flight.icao24,
            }
        )

    df = pd.DataFrame(flights_data)
    df.to_csv(
        "data/flights_by_aircraft.csv",
        mode="a",
        header=False,
        index=False,
    )
    print("flights have been saved to 'data/flights_by_aircraft.csv'.")
    pass


def get_flight_interval(api, begin, end):
    interval = api.get_flights_from_interval(begin, end)

    if not interval:
        return print(f"Return None from interval: {interval}")

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
                "icao24": inte.icao24,
                "lastSeen": inte.lastSeen,
            }
        )

    df = pd.DataFrame(intervals)
    df.to_csv(
        "data/flights_by_interval.csv",
        mode="a",
        header=False,
        index=False,
    )
    pass


if __name__ == "__main__":
    now = datetime.now()
    last_hour = now - timedelta(minutes=60)
    unix_hour = int(last_hour.timestamp())
    unix_now = int(now.timestamp())
    api = OpenSkyApi("hadhatter", "287a6655aa625870d39b8acb2a852d25")
    airports = ["KATL", "KSLC", "KDFW", "KDEN", "KORD", "OMDB"]

    # craft_ids_csv = pd.read_csv("data/icao24_craft_ids.csv")
    # craft_ids_df = pd.DataFrame(craft_ids_csv)
    # craft_ids = craft_ids_df.sample(n=6).to_list()

    # print(craft_ids)

    get_states(api)
    get_flights_by_aircraft(api, "3c4b26", unix_hour, unix_now)
    get_flight_interval(api, unix_hour, unix_now)
    for ap in airports:
        get_arrivals(api, ap, unix_hour, unix_now)
    for ap in airports:
        get_departures(api, ap, unix_hour, unix_now)
# HERE GIVE THE icao24 AND DATES IN UNIX TIMESTAMP FORMATION
