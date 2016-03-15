"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    return urllib2.urlopen(url)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    f = get_json(GMAPS_BASE_URL+urllib.urlencode({'address':place_name}))
    data = json.loads(f.read())
    try:
        return (data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng'])
    except IndexError:
        raise IndexError("Location not found!")

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    f = get_json(MBTA_BASE_URL+urllib.urlencode({"api_key":MBTA_DEMO_API_KEY,"lat":latitude,"lon":longitude,"format":"json"}))
    data = json.loads(f.read())
    try:
        return (data['stop'][0]['stop_name'], data['stop'][0]['distance'])
    except IndexError:
        raise IndexError("No stations were found near {},{}".format(latitude, longitude))

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    station = get_nearest_station(*get_lat_long(place_name))
    print "Station:  "+station[0]
    print "Distance: "+str(int(float(station[1])*1609.34))+" m"


find_stop_near("4 Yawkey Way, Boston, MA 02215")