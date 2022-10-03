import os
import requests
import urllib.parse

from dotenv import load_dotenv
load_dotenv()


def get_places_from_search(search):
    """Get places results from search term"""

    api_url = "https://api.os.uk/search/places/v1/find?"
    params = {"query": search, 'key': os.environ.get(
        "os_api_key"), 'maxresults': '30'}
    response = requests.get(api_url + urllib.parse.urlencode(params))
    json = response.json()['results']

    fresh_addresses = []

    for value in json:
        fresh_addresses.append(value['DPA'])
    return fresh_addresses
