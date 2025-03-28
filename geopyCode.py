
# Geopy
"""
this is for getting coordinates from an address 
"""

from geopy.geocoders import Nominatim # https://geopy.readthedocs.io/en/stable/
#https://stackoverflow.com/questions/60928516/get-address-from-given-coordinate-using-python
#https://geopy.readthedocs.io/en/stable/#module-geopy.geocoders
#https://github.com/DenisCarriere/geocoder/blob/master/README.md
#https://geocoder.readthedocs.io/results.html

def get_coordinates(place):
    """Function to get latitude and longitude from an address"""
    geolocator = Nominatim(user_agent="GetLoc") #https://www.youtube.com/watch?v=mhTkaH2YuAc
    location = geolocator.geocode(
        place, # Robert Vance Residence Hall
        country_codes="us",  # Restrict search to the US
        viewbox=[(42.050587,-73.727775), (40.950943, -71.787220)],  # Bounding box for Connecticut
        bounded=True  # Ensures results stay within the viewbox
    )
    if location:
        #print((location.latitude, location.longitude)) # Debugging. Outputs Lat and Lon.
        #print(location.address) # Debugging. Outputs full Address
        print(location.raw) # Debugging. # full data pull
        return location.latitude, location.longitude # outputs Lat and Long for API use.
    else: return None #print("Location not found within Connecticut.") # outputs nothing

def main():
    strUserInputLocation = input("Enter a location (try 'Vance Hall'): ") # Debug = "Vance Hall"#
    lat , lon = get_coordinates(strUserInputLocation)
    # Assigns returned location.latitude,location.longitude to lat,lon
    print(lat) #Debug
    print(lon) #Debug

main()
