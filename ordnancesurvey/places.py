import os
import requests
import urllib.parse

from dotenv import load_dotenv
load_dotenv()

def get_places_from_search(search):
    """Get places results from search term"""
    fresh_addresses = []
    api_url = "https://api.os.uk/search/places/v1/find?"
    params = {"query": search, 'key': os.environ.get(
        "os_api_key"), 'maxresults': '30'}
    response = requests.get(api_url + urllib.parse.urlencode(params))

    if 'results' in response.json():
        json = response.json()['results']
        for value in json:
            fresh_addresses.append(value['DPA'])
            
    return fresh_addresses

def get_building_from_toid(toid):
    fresh_addresses = []
    """Get building results from TOID term thru UPRN"""
    linked_ident_api_url = f"https://api.os.uk/search/links/v1/identifierTypes/TOID/{toid}?"
    params = {'key': os.environ.get("os_api_key")}
    response = requests.get(linked_ident_api_url + urllib.parse.urlencode(params))
    json_uprn = response.json()
    if 'correlations' in json_uprn: 
        uprn = int(json_uprn['correlations'][0]['correlatedIdentifiers'][0]['identifier'])
        places_api_url  = "https://api.os.uk/search/places/v1/uprn?"
        params = {"uprn": uprn, 'key': os.environ.get("os_api_key")}
        response = requests.get(places_api_url + urllib.parse.urlencode(params))

        if 'results' in response.json():
            json = response.json()['results']
            for value in json:
                fresh_addresses.append(value['DPA'])

    return fresh_addresses