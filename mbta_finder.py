"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

When inputting address, follow this format:
House Number, Street Direction, Street Name, Street Suffix, City, State, Zip, Country

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
GMAPS_API_KEY = "AIzaSyBrHpczS7mYZMJY1hOC8qkRVXztQ-sxb7Q"


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
    address = place_name.replace(" ", ",")
    url = "{}?address={}&key={}".format(GMAPS_BASE_URL, address, GMAPS_API_KEY)
    response = get_json(url)
    coordinates = response["results"][0]["geometry"]["location"]
    res = [(b) for a, b in coordinates.iteritems()]
    return res


def get_nearest_station(place_name):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    coordinates = get_lat_long(place_name)
    url = "{}?api_key={}&lat={}&lon={}&format=json".format(MBTA_BASE_URL, MBTA_DEMO_API_KEY, str(coordinates[0]), str(coordinates[1]))
    response = get_json(url)
    nearest_station = response["stop"][0]["stop_name"]
    distance = response["stop"][0]["distance"]
    res = (nearest_station, distance)
    return res


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    try:
        closest_stop = get_nearest_station(place_name)
        listed_stop = list(closest_stop)
        statement = "Nearest MBTA Stop: {}\nDistance to Stop: {} miles".format(closest_stop[0], closest_stop[1])
        return statement
    except:
        return "There are no MBTA stops near {}.".format(place_name)

# print find_stop_near("Needham Center")