from flask import Flask
import os
from dotenv import load_dotenv
import requests
import urllib.parse

load_dotenv()


app = Flask(__name__)


@app.route("/autofill/<input>")

def free_test_places(input):
    api_url = "https://api.os.uk/search/places/v1/find?"
    params = {"query":input, 'key': os.environ.get("os_api_key"),'maxresults': '30'}
    # print(api_url + urllib.parse.urlencode(params))
    response = requests.get(api_url + urllib.parse.urlencode(params))
    json = response.json()['results']
    fresh_address = {}

    for value in json:
        fresh_address[value['DPA']['UPRN']] = value['DPA']
    return fresh_address


def hello_world():
    return "Hello, World!"
