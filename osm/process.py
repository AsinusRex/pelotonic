# This file contains the functions that can take the OSM data and convert it into a graph to be loaded into mongo.

def process(raw_osm_data):
    """
    Processes raw OSM data to produce structured graph data:
        1. Parses OSM ways and nodes.
        2. Constructs an edge list representation with OSM node IDs for graph vertices.
        3. Each edge includes start_node, end_node, length, road type, and other attributes.
        4. Returns structured graph data ready for insertion into MongoDB.
    """
    pass