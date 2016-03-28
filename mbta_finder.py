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

GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GMAPS_API_KEY = "AIzaSyBAbkJTjX3Vk0eorBNKFAlIlbyH7NC4frg"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

def get_gmaps_url(location):
    """
    Gives the url needed for the Google Maps API for a given location.
    """
    url = GMAPS_BASE_URL + '?address='
    words = location.split(' ')
    for word in words[0:-1]:
        url = url + word + '%20'
    url = url + words[-1] + '&key=' + GMAPS_API_KEY
    return url

def get_mbta_url(lat, lon):
    """
    Gives the url needed for the mbta API for a given latitude and longitude
    """
    return MBTA_BASE_URL + '?api_key=' + MBTA_DEMO_API_KEY + '&lat=' + str(lat) + '&lon=' + str(lon) + '&format=json'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    return json.loads(response_text)

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    url = get_gmaps_url(place_name)
    response_data = get_json(url)
    latitude = response_data[u'results'][0][u'geometry'][u'location'][u'lat']
    longitude = response_data[u'results'][0][u'geometry'][u'location'][u'lng']
    return (latitude, longitude)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = get_mbta_url(latitude, longitude)
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    distance = response_data[u'stop'][0][u'distance']
    stop_name = response_data[u'stop'][0][u'stop_name']
    return (stop_name, distance)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    >>>find_stop_near('Faneuil Hall')
    The nearest stop is Congress St @ North St, which is 0.0524380765855312 miles away.
    """
    (lat, lon) = get_lat_long(place_name)
    (stop_name, distance) = get_nearest_station(lat,lon)
    print 'The nearest stop is ' + stop_name + ', which is ' + distance + ' miles away.'