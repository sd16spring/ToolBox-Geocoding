"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
import requests # this is SO much better than urllib in SO many ways! go try it, NINJAS! in particular you don't have to do
#things like make spaces = %20 it just behaves in a more user friendly way and errors less
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "?api_key=wX9NwuHnZU2ToO7GmGR9uw"
GOOGLE_MAP_APIKEY = '&key=AIzaSyDunQEat_x1SofgLwhMHPkC4mnHPlXSjS0'


# A little bit of scaffolding if you want to use it


def make_googlemap_url(name, state):
    """ helper function which takes a name and state and formats it to be a url"""
    name_state_combo = '?address=' + name + '&components=administrative_area:' + state
    url = GMAPS_BASE_URL + name_state_combo  +   GOOGLE_MAP_APIKEY
    return url



def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    stuff = requests.get(url)
    response_text = stuff.text
    response_data = json.loads(response_text)
    return response_data



def get_lat_long(json_data):
    """
    Given the data that was retrieved using the place name/address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.

    """

    lat_long_raw = (json_data["results"][0]['geometry']['location']) #[0]["location"]
    lat = lat_long_raw.get('lat')
    long = lat_long_raw.get('lng')
    lat_long_tuple = (lat,long)
    return lat_long_tuple


def make_mbta_url(lat_long_tuple):
    """makes an appropriate mbta url with the latitude and longitude tuple given (returns the url string)"""
    long_lat = '&lat=' + str(lat_long_tuple[0]) + '&lon=' + str(lat_long_tuple[1]) + '&format=json'
    url = MBTA_BASE_URL + MBTA_DEMO_API_KEY + long_lat
    return url




def get_nearest_station(lat_long_tuple):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = make_mbta_url(lat_long_tuple)
    data= get_json(url)

    #station_name = data[0]
    #distance = data

    distance = data['stop'][0]['distance']
    station_name = data['stop'][0]['stop_name']
    return (str(station_name), str(distance))



def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    state = 'MA' #because this is the MBTA - makes google stop tellng me about the fenways in texas!
    googlemap_url =  make_googlemap_url(place_name, state)
    google_data = get_json(googlemap_url)
    lat_long_tuple = get_lat_long(google_data)
    name_dist_tuple= get_nearest_station(lat_long_tuple)
    return name_dist_tuple

name_distance_tuple= find_stop_near('Fenway Park')
print name_distance_tuple

