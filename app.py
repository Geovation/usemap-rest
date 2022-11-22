from flask import Flask, jsonify
from ordnancesurvey import places, features, linkedids

app = Flask(__name__)


@app.route("/places/<input>")
def get_places(input):
    return jsonify(places.get_places_from_search(input))

@app.route("/places/toid/<input>")
def get_toid_building(input):
    return jsonify(places.get_building_from_toid(input))

@app.route("/features/<input>")
def get_feature(input):
    return jsonify(features.get_feature_from_toid(input))

@app.route("/features/ngd/<input>")
def get_feature_ngd(input):
    return jsonify(features.get_feature_from_toid_ngd(input))

@app.route("/linkedids/uprn/<input>")
def get_linked_ids(input):
    return jsonify(linkedids.get_linked_ids_from_uprn(input))