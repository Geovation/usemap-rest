import os
import requests
import urllib.parse
from osdatahub import NGD
import geojson


from dotenv import load_dotenv
load_dotenv()

def get_feature_from_toid(toid):
    """Get feature from given TOID"""
    xml = '<ogc:Filter>'
    xml += '<ogc:PropertyIsEqualTo>'
    xml += '<ogc:PropertyName>TOID</ogc:PropertyName>'
    xml += '<ogc:Literal>' + toid + '</ogc:Literal>'
    xml += '</ogc:PropertyIsEqualTo>'
    xml += '</ogc:Filter>'

    wfs_params = {
        'key': os.environ.get("os_api_key"),
        'service': 'WFS',
        "request": 'GetFeature',
        "version": '2.0.0',
        "typeNames": 'Topography_TopographicArea',
        "propertyName": 'TOID,DescriptiveGroup,SHAPE,Theme,ChangeDate,ChangeHistory,CALCULATEDAREAVALUE',
        "outputFormat": 'GEOJSON',
        "filter": xml,
        "count": 1
    }

    api_url = "https://api.os.uk/features/v1/wfs?"
   
    response = requests.get(api_url + urllib.parse.urlencode(wfs_params))
    json = response.json()
    return json

def get_feature_from_toid_ngd(toid):
    cql = "toid = '"+ toid + "'"

    NGD.get_collections()
    collection = 'bld-fts-buildingpart'
    ngd = NGD(os.environ.get("os_api_key"), collection)
    results = ngd.query(cql_filter=cql, max_results=10)
    return results