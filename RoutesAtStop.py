
"""
this code is for the display of routes at a stop.
"""

import requests
from datetime import datetime, UTC, timedelta

# from pytz import timezone
# tz = timezone('EST')
# https://stackoverflow.com/questions/11710469/how-to-get-python-to-display-the-current-eastern-time

# -4 hr to account for EST

# Read's API.txt to keep the API out of the code.
def api_key():
    try:
        with open("API.txt", "r") as file:
            API_KEY = file.read()
            if not API_KEY:
                raise ValueError("API key is empty")
            return API_KEY
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        exit()
# tries to read API.txt. this is to prevent the API key from being hard coded into program.

def max_distance():
    return 1500

def output(): # replace this with the geopy code
    lat, lon = 41.53893285402787, -72.80120743546017 # meriden station
    # 45.526168077787894, -73.59506067289408
    # (41.69367820450357, -72.76272775194853) # vance building
        #41.53893285402787, -72.80120743546017) #debug - meriden station commuter parking
    # 41.7656200, -72.6727190 # Central Row
    return lat, lon

def get_routes_at_stop(lat, lon):
    url = "https://external.transitapp.com/v3/public/nearby_routes"
    headers = {"apiKey": api_key()}
    params = {
        "lat": lat,
        "lon": lon,
        "max_distance": max_distance(),
        "should_update_realtime": True
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json().get("routes", []) if response.status_code == 200 else []


def main():
    latitude, longitude = output()
    routes = get_routes_at_stop(latitude, longitude)
    # print(f"For Stop at {routes}:") # Debug
    for route in routes:
        route_short_name = route.get("route_short_name", "Unknown")
        next_departure = None

        for itinerary in route.get("itineraries", []):
            for schedule in itinerary.get("schedule_items", []):
                timestamp = schedule["departure_time"]
                if next_departure is None or timestamp < next_departure:
                    next_departure = timestamp

        if next_departure:  # Convert UTC to EST (-5 hours)
            est_time = datetime.fromtimestamp(next_departure, UTC) - timedelta(hours=4)
            formatted_time = est_time.strftime('%I:%M %p')  # 12-hour format with AM/PM
            formatted_date = est_time.strftime('%B %d')  # %B is the datetime variable for %m written out.
            print(f"{formatted_date} Route {route_short_name}, Next Departure Time - {formatted_time}")
            return formatted_date, formatted_time, route_short_name
        """
        # basic start output.
        if next_departure:  # Convert UTC to EST (-5 hours)
            est_time = datetime.fromtimestamp(next_departure, UTC) - timedelta(hours=4)
            formatted_time = est_time.strftime('%Y-%m-%d %H:%M:%S')
            print(f"Route: {route_short_name}.  Next Departure Time (EST): {formatted_time}")
        """

main()
