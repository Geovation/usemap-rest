import os
from osdatahub import NGD


from dotenv import load_dotenv
load_dotenv()


def get_building_feature_from_toid(toid):
    """Get a building feature from the OS National Geographic Database using the Topographic Identifier"""

    cql_query = "toid = '" + toid + "'"

    NGD.get_collections()
    collection = 'bld-fts-buildingpart'
    ngd = NGD(os.environ.get("os_api_key"), collection)
    results = ngd.query(cql_filter=cql_query, max_results=10)

    return results
