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
# url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
# f = urllib2.urlopen(url)
# response_text = f.read()
# response_data = json.loads(response_text)
# pprint(response_data)
# print response_data["results"][0]["formatted_address"]


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
GMAPS_API_KEY = 'AIzaSyDvLrXdD3pmGbvsc4MJa8DuUmv4Cd2vc_o'
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    pass
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
    pass
    # poi = place_name.replace(' ','%20')
    address = place_name.replace(' ','+')
    url = GMAPS_BASE_URL + '?address=' + address + '&key=' + GMAPS_API_KEY
    # print url
    # break
    response_data = get_json(url)
    latitude = str(response_data["results"][0]["geometry"]["location"]['lat'])
    longitude = str(response_data["results"][0]["geometry"]["location"]['lng'])
    return (latitude,longitude)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    pass
    url = MBTA_BASE_URL + '&key=' + MBTA_DEMO_API_KEY + '&lat=' + latitude + '&lon=' + longitude + '&format=json/'
    # nearby = stopsbylocation(latitude,longitude)
    nearby = get_json(url)
    station_name = str(nearby['stop'][0]['stop_name'])
    distance = str(nearby['stop'][0]['distance'])
    return (station_name,distance)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    pass
    location = get_lat_long(place_name)
    return get_nearest_station(location[0],location[1])

find_stop_near('Faneuil Hall')
