"""
Updated March 20, 2016

Find the MBTA stops closest to a given location. Prints the
closest MBTA stop and the distance from the given place to that stop.

@author: Erica Lee
"""

import urllib, urllib2,json
from pprint import pprint


GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    

    return response_data["results"][0]["geometry"]["location"]


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
     
    """
    
    g = {}  
    g["address"] = place_name
    g =sorted(g.iteritems())
    

    url = GMAPS_BASE_URL + urllib.urlencode(g)
    
    coord = get_json(url)
    return coord




def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    """
    i = {}
    i['lat'] = latitude
    i['lon'] = longitude
    i['api_key'] = MBTA_DEMO_API_KEY

    i = sorted(i.iteritems())
    url2 = MBTA_BASE_URL + urllib.urlencode(i)

    h = urllib2.urlopen(url2)
    response_text = h.read()
    response_data = json.loads(response_text)
    
    a = response_data["stop"][0]["stop_name"]
    b = response_data["stop"][0]["distance"]
    
    return (str(a),str(b))
    


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    coordinates = get_lat_long(place_name).values()
    stop = get_nearest_station(coordinates[0], coordinates[1])[0]
    distance = get_nearest_station(coordinates[0], coordinates[1])[1]

    return "%s is %s miles away from %s"%(stop, distance, place_name)


print find_stop_near("Fenway Park MA")
