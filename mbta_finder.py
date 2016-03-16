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
	url: url of the API request
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
    place_name: address of place to look up
    """
    place_name_f = place_name.replace(' ', '+')
    place_url = GMAPS_BASE_URL + '?address={kwarg}&components=administrative_area:MA|country:US'.format(kwarg=place_name_f)
    latitude = get_json(place_url)["results"][0]["geometry"]["location"]["lat"]
    longitude = get_json(place_url)["results"][0]["geometry"]["location"]["lng"]
    return (latitude, longitude)

def get_nearest_station(latitude, longitude):
	"""
	Given latitude and longitude strings, return a (station_name, distance)
	tuple for the nearest MBTA station to the given coordinates.

	See http://realtime.mbta.com/Portal/Home/Documents for URL
	formatting requirements for the 'stopsbylocation' API.
	latitude, longitude: geographic coordinates of the place to find nearest station to
	"""
	key = MBTA_DEMO_API_KEY
	station_url = MBTA_BASE_URL + '?api_key={}&lat={}&lon={}&format=json'.format(key, str(latitude), str(longitude))
	try:
		station_name = get_json(station_url)["stop"][0]["stop_name"]
		distance = get_json(station_url)["stop"][0]["distance"]
		distance_f = str(round(float(distance), 2)) 
		return (station_name, distance_f)
	except:
		return 'No stations close by'


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    place_name: address of place to lookup
    """
    lat = get_lat_long(place_name)[0]
    lon = get_lat_long(place_name)[1]
    return get_nearest_station(lat, lon)



