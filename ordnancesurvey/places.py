import os
import requests
import urllib.parse

from dotenv import load_dotenv
load_dotenv()


def get_places_from_search(search):
    """Get place results from a text search via the places API"""

    places = []
    api_url = "https://api.os.uk/search/places/v1/find?"
    params = {"query": search, 'key': os.environ.get(
        "os_api_key"), 'maxresults': '30'}
    response = requests.get(api_url + urllib.parse.urlencode(params))

    if 'results' in response.json():
        json = response.json()['results']
        for value in json:
            places.append(value['DPA'])

    return places


def get_places_from_uprn(uprn):
    """Get place results from a UPRN via the places API"""

    places = []
    api_url = "https://api.os.uk/search/places/v1/uprn?"
    params = {'uprn': uprn, 'key': os.environ.get("os_api_key")}
    response = requests.get(api_url + urllib.parse.urlencode(params))
    
    if 'results' in response.json():
        json = response.json()['results']
        for value in json:
            places.append(value['DPA'])

    return places
