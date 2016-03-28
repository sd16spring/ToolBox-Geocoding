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
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw"
GMAPS_API_KEY = "AIzaSyCoT-0Iv49u3-Sz2T5O4T8xYer8E16BGrw"


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
    formatted_place_name = place_name.replace(' ','+')
    request_url = GMAPS_BASE_URL + "?address=" + formatted_place_name + "&key=" + GMAPS_API_KEY
    response_data = get_json(request_url)
    #return latitude and longitude
    return (str(response_data["results"][0]["geometry"]["location"]["lat"]),str(response_data["results"][0]["geometry"]["location"]["lng"]))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = MBTA_BASE_URL + "&lat=" + latitude + "&lon=" + longitude + "&format=json"
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    station_name = response_data["stop"][0]["stop_name"]
    distance = response_data["stop"][0]["distance"]
    return (station_name,distance)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat,lon = get_lat_long(place_name)
    station_name,distance = get_nearest_station(lat,lon)
    print "The nearest station is " + station_name + ", " + distance + " miles away."

