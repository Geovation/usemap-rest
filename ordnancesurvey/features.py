import os
import requests
import urllib.parse
from osdatahub import NGD
import geojson


from dotenv import load_dotenv
load_dotenv()

def get_feature_from_toid(toid):
    cql = "toid = '"+ toid + "'"

    NGD.get_collections()
    collection = 'bld-fts-buildingpart'
    ngd = NGD(os.environ.get("os_api_key"), collection)
    results = ngd.query(cql_filter=cql, max_results=10)
    return results