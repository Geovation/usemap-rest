import os
from flask import Flask, jsonify
from flask_cors import CORS
from ordnancesurvey import places, features, linkedids

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
origin = os.environ.get("cors_origin")
CORS(app, origins=origin)


@app.route("/features/toid/<input>")
def get_feature(input):
    return jsonify(features.get_building_feature_from_toid(input))


@app.route("/places/<input>")
def get_places_from_search(input):
    return jsonify(places.get_places_from_search(input))


@app.route("/places/toid/<input>")
def get_places_from_toid(input):
    json_uprn = linkedids.get_linked_ids_from_toid(input)
    if 'correlations' in json_uprn:
        uprn = int(json_uprn['correlations'][0]
                   ['correlatedIdentifiers'][0]['identifier'])
        return jsonify(places.get_places_from_uprn(uprn))
    else:
        return jsonify([])


@app.route("/linkedids/uprn/<input>")
def get_linked_ids(input):
    return jsonify(linkedids.get_linked_ids_from_uprn(input))
