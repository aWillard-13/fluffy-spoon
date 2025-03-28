# No GUI


# get_coordinates
# get_nearby_bus_stops

"""
this code uses the Transit App API, 
gets the coordinates from a user input address,
and gets nearby bus stops from the Transit App API.
"""

api_key = [key] # put key here.
#call later uses of api_key()

from geopy.geocoders import Nominatim # https://geopy.readthedocs.io/en/stable/
import requests # https://www.w3schools.com/python/module_requests.asp

def get_coordinates(place):
    """Function to get latitude and longitude from an address"""
    geolocator = Nominatim(user_agent="GetLoc") #https://www.youtube.com/watch?v=mhTkaH2YuAc
    location = geolocator.geocode(
        place,
        country_codes="us",  # Restrict search to the US
        viewbox=[(42.050587,-73.727775), (40.950943, -71.787220)],  # Bounding box for Connecticut
        bounded=True  # Ensures results stay within the view box
        # everything here is learned from the documentation
    )
    if location:
        #print((location.latitude, location.longitude)) # Debugging. Outputs Lat and Lon.
        #print(location.raw) # Debugging. # full data pull
        return location.latitude, location.longitude # outputs Lat and Long for API use.
    else: return None #"Location not found within Connecticut." # outputs nothing

def max_distance():
    return 1000

def get_nearby_bus_stops(lat, lon, stop_filter="Routable", pickup_dropoff_filter="Everything"):
    """API Get function."""
    if lat is None or lon is None:  # Prevent API call with invalid coordinates
        print("Invalid coordinates. Cannot fetch bus stops.")
        return None
    url = "https://external.transitapp.com/v3/public/nearby_stops" # URL for the Transit App API endpoint
    # Headers for the request
    headers = {"apiKey": api_key } #actual key is put in main
    # Parameters to be sent in the API request (latitude, longitude, max_distance, etc.)
    params = {
        "lat": lat, # NEEDED FOR API
        "lon": lon, # NEEDED FOR API
        "max_distance": max_distance(),
        "stop_filter": stop_filter, # extra to help narrow search
        "pickup_dropoff_filter": pickup_dropoff_filter # extra to help narrow search
    }

    try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200: #200 code is a successful call per their API docs
                data = response.json()
                # print(data) # Debug
                # Ensure "stops" key exists and is non-empty before accessing
                if "stops" in data and len(data["stops"]) > 0:
                    first_stop = data["stops"][0]
                    return first_stop.get("stop_lat"), first_stop.get("stop_lon"), first_stop.get("stop_name")
                else:
                    print("No bus stops found.")
                    return None
            else:
                print(f"Error: {response.status_code}")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # User Input
    strUserInputLocation = input("Enter a location (try 'Vance Hall'): ") # Debug = "Vance Hall"#
    # Assigns returned location.latitude,location.longitude to lat,lon
    latitude , longitude = get_coordinates(strUserInputLocation)
    if latitude is not None and longitude is not None:
        nearby_bus_stops = get_nearby_bus_stops(latitude, longitude)
        if nearby_bus_stops: print("Nearby Bus Stop:", nearby_bus_stops)
    else: print("Location not found. Please try again.")

main()
