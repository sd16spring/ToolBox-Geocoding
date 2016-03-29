"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

API Key:  AIzaSyBIS2m7-pBDH4hnIOlTd5bNGtnqboGGUZM 

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint
import str


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
My_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?address=[number+street+type],[+cityname],[+state]&key=AIzaSyBIS2m7-pBDH4hnIOlTd5bNGtnqboGGUZM"


# A little bit of scaffolding if you want to use it

def make_url(place_name):
    """
    Given a place name or address, return a url that will open the necessary API
    place name must be in string format, "number+street+type,+cityname,+state"
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + place_name + "&key=AIzaSyBIS2m7-pBDH4hnIOlTd5bNGtnqboGGUZM"
    return url

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

    place name must be in string format, "number+street+type,+cityname,+state"

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
   	url = make_url(place_name)
    data = get_json(url)
    coordinates = (data["results"]["geometry"]["location"]["lat"], data["results"][0]["geometry"]["location"]["lat"])
    return coordinates

def get_nearest_station(place_name):
    """
    Given a place name,  return a (station_name, distance)
    tuple for the nearest MBTA station to the coordinates of the given place
    """
    coordinates = get_lat_long(place_name)
    latitude = str(coordinates[1])
    longitude = str(coordinates[2])
    lat.lng = "&lat=" + latitude +"&lon=" + longitude
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?" + lat.lng + "&format=json"
    data = get_json(url)
    nearest_stop_name = ["stop"][0]["stop_name"]
    distance = ["stop"][0]["distance"]
    station = (nearest_stop_name, distance)