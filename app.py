from flask import Flask, jsonify
from ordnancesurvey import places

app = Flask(__name__)


@app.route("/places/<input>")
def get_places(input):
    return jsonify(places.get_places_from_search(input))
