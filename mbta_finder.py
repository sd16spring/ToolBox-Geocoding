"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json

# Useful URLs
gmaps_base_url = "https://maps.googleapis.com/maps/api/geocode/json"
mbta_base_url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
mbta_api_key = "wX9NwuHnZU2ToO7GmGR9uw"

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f=urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    # pprint (response_data)
    # print response_data["results"][0]["formatted_address"]
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    new_place_name = place_name.replace(' ', '+')
    url_of_place = gmaps_base_url + '?address={kwarg}&components=administrative_area:MA|country:US'.format(kwarg=new_place_name)
    get_info = get_json(url_of_place)
    lat_coordinate = get_info["results"][0]["geometry"]["location"]["lat"]
    lon_coordinate = get_info["results"][0]["geometry"]["location"]["lng"]
    # print (lat,lon)
    return (lat_coordinate, lon_coordinate)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url_of_station = mbta_base_url + '?api_key={}&lat={}&lon={}&format=json'.format(mbta_api_key, str(latitude), str(longitude))
    get_info = get_json(url_of_station)
    station_name = get_info["stop"][0]["stop_name"]
    dist = get_info["stop"][0]["distance"]
    formatted_dist = round(float(dist), 2)
    distance = str(formatted_dist) 
    # print (station_name, distance)
    return (station_name, distance)

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat = get_lat_long(place_name)[0]
    lon = get_lat_long(place_name)[1]
    # print get_nearest_station(lat,lon)
    station_name = get_nearest_station(lat, lon) [0]
    distance = get_nearest_station(lat, lon) [1]
    return "The closest MBTA stop to %s is %s miles away at %s" % (place_name, distance, station_name)

# command that takes a place name or address as input, finds its latitude/longitude, 
# and returns the nearest MBTA and its distance from the starting point.
print find_stop_near('Boston Commons')