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
import math
from geopy.distance import great_circle

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
    place_name = place_name.replace(' ','+')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+place_name+'&key=AIzaSyDkALHr48F_NL-kvKIzFFPvpZ_iaW2AgSM'
    response_data = get_json(url)
    latitude = response_data["results"][0]["geometry"]["location"]["lat"]
    longitude = response_data["results"][0]["geometry"]["location"]["lng"]
    return latitude,longitude


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat='+str(latitude)+'&lon='+str(longitude)+'&format=json'
    print url
    response_data = get_json(url)
    station = response_data["stop"][0]["stop_lat"],response_data["stop"][0]["stop_lon"]
    station_name = response_data["stop"][0]["stop_name"]
    location = (latitude,longitude)
    return station_name,great_circle(station,location).miles




def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    latitude,longitude = get_lat_long(place_name)
    station_name,distance = get_nearest_station(latitude,longitude)
    print station_name
    print distance

find_stop_near('900 Boylston St, Boston, MA 02115')