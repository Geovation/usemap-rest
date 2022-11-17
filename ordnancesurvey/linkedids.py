import os
import requests
import urllib.parse

from dotenv import load_dotenv
load_dotenv()

def get_linked_ids_from_uprn(uprn):
    """Get linked identifiers from a given UPRN"""
    
    json = {}
    api_url = f"https://api.os.uk/search/links/v1/identifierTypes/UPRN/{uprn}"
    params = {'key': os.environ.get("os_api_key")}
    response = requests.get(api_url + urllib.parse.urlencode(params))
    json = response.json()
    print(response.json())
    
    return json