"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data
 

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    processed_name = ["+" if c == " " else c for c in place_name]
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + "".join(processed_name) # + "&key=" + 
    infodump = get_json(url)
    return (infodump['results'][0]['geometry']['location']['lat'],infodump['results'][0]['geometry']['location']['lng'])

# pprint(get_lat_long("Fenway Park, Massachusetts"))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=" + MBTA_DEMO_API_KEY + "&lat=" + str(latitude) + "&""lon=" + str(longitude) + "&format=json"
    infodump = get_json(url)
    return (str(infodump['stop'][0]['stop_name']),str(infodump['stop'][0]['distance']) + " miles")
# geoinfo = get_lat_long("Fenway Park, Massachusetts")
# print(get_nearest_station(geoinfo[0],geoinfo[1]))


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    location = get_lat_long(place_name) #location is a (lat,long) tuple
    return "Location: " + str(location) + "\n" + "Stop: " + str(get_nearest_station(location[0],location[1]))

print find_stop_near("Fenway Park, Massachusetts")

