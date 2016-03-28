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
import urllib


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
GMAPS_API_KEY = 'AIzaSyCrfI3z_PcorRZ-nCJl3T0NKfl4zU6eDFM'


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)

    
    return (response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    address = place_name.replace(" ", ",")

    place_url = GMAPS_BASE_URL + '?' + 'address=' + address + GMAPS_API_KEY
    
    response_data = get_json(place_url)
    latlng = response_data["results"][0]["geometry"]["location"]
    
    return (latlng.get(u'lat'), latlng.get(u'lng'))



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    try:
        stop_nearby_url = '{}?api_key={}&lat={}&lon={}&format=json'.format(MBTA_BASE_URL, MBTA_DEMO_API_KEY, latitude, longitude)
        
        data = get_json(stop_nearby_url)
        info = data[u'stop'][0]
        place_info = [info.get(u'parent_station_name'), info.get(u'distance')]
        station_name = place_info[0].replace('u', '')
        distance = place_info[1].replace('u', '')
    
        name_dist = (station_name, distance)
        print station_name + ' is ' + distance + ' miles away.'

    except:
        "There are no T-stops close by."


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    latlng_place = get_lat_long(place_name)

    get_nearest_station(latlng_place[0], latlng_place[1])


find_stop_near('Boston University')

