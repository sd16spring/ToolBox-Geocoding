"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""
"""
Completed by Kevin Zhang
Software Design Spring 2016
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


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

    place = place_name.replace(" ", "+")
    url = GMAPS_BASE_URL + "?address=" + place
    json_data = get_json(url)
    lat = json_data["results"][0]["geometry"]["location"]["lat"]
    lon = json_data["results"][0]["geometry"]["location"]["lng"]

    return lat, lon


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = MBTA_BASE_URL + "?api_key=" + MBTA_DEMO_API_KEY + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&format=json"
    json_data = get_json(url)


    station_name = json_data["stop"][0]["stop_name"]
    distance = json_data["stop"][0]["distance"]

    return station_name, distance



def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat, lng = get_lat_long(place_name)
    print "The location you gave is at " + str(lat) + " latitude and " + str(lng) + " longitude."
    print ''

    station_name, distance = get_nearest_station(lat, lng)
    print "The nearest MBTA station to that location is " + str(station_name) + ", which is {:.4f} miles away.".format(float(distance))
    print ''
    


if __name__ == "__main__":

    done = False
    count = 0
    while not done:
        if count == 0:
            place = raw_input("Please type in the a location to determine your nearest MBTA Station (National Post Service format please!)\n\n")
            count +=1
        else:
            place = raw_input("Wanna type in another location to find the nearest MBTA?\n\n")


        if place == "done":
            print "Thanks for using me!"
            done = True
        else:
           find_stop_near(place)
