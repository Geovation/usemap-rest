from flask import Flask, jsonify
from ordnancesurvey import places, features

app = Flask(__name__)


@app.route("/places/<input>")
def get_places(input):
    return jsonify(places.get_places_from_search(input))

@app.route("/places/toid/<input>")
def get_toidbuilding(input):
    return jsonify(places.get_building_from_toid(input))

@app.route("/features/<input>")
def get_feature(input):
    return jsonify(features.get_feature_from_toid(input))

