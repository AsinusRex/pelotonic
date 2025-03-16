from pyproj import Transformer
from pymongo import GEOSPHERE
import logging

class AreaData:

    @staticmethod
    def write_graph_to_db(db, nodes, edges):
        nodes_collection = db["osm_nodes"]
        edges_collection = db["osm_edges"]

        if nodes:
            nodes_collection.insert_many(nodes, ordered=False)
            logging.info("%d nodes stored.", len(nodes))

        if edges:
            edges_collection.insert_many(edges, ordered=False)
            logging.info("%d edges stored.", len(edges))

        nodes_collection.create_index([("location", GEOSPHERE)])

    @staticmethod
    def check_in_db(db, bbox):
        """Check if we have data for the entire bounding box"""
        query = {
            "location": {
                "$geoWithin": {
                    "$geometry": {
                        "type": "Polygon",
                        "coordinates": [[
                            [bbox["min_lon"], bbox["min_lat"]],
                            [bbox["max_lon"], bbox["min_lat"]],
                            [bbox["max_lon"], bbox["max_lat"]],
                            [bbox["min_lon"], bbox["max_lat"]],
                            [bbox["min_lon"], bbox["min_lat"]]
                        ]]
                    }
                }
            }
        }

        complete = db.osm_nodes.find_one(query) is not None
        logging.info("Area coverage complete: %s", complete)
        return complete