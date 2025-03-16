import logging
from db import db
from config.config import load_config
from osm import osm

def orchestrate_request(origin_lat, origin_lon, dest_lat, dest_lon, user_id):
    """Orchestrates the route request flow"""
    config = load_config()
    database = db.connect(
        config.get("MONGO_URI"),
        config.get("DB_NAME")
    )
    if database is None:
        logging.error("Database connection failed in orchestration.")
        return {"error": "Database connection failed."}

    user_props = db.get_user(database, user_id)
    if not user_props:
        logging.error("User data not found for user ID: %s", user_id)
        return {"error": "User data not found."}

    # Add buffer around the bounding box (approximately 500 meters)
    buffer = 0.005  # rough approximation in degrees
    bbox = {
        "min_lat": min(origin_lat, dest_lat) - buffer,
        "max_lat": max(origin_lat, dest_lat) + buffer,
        "min_lon": min(origin_lon, dest_lon) - buffer,
        "max_lon": max(origin_lon, dest_lon) + buffer
    }

    # Check and fetch data if needed
    complete = db.check_in_db(database, bbox)
    if not complete:
        logging.info("Fetching OSM data for bounding box")
        g = osm.fetch([bbox])
        if isinstance(g, str):
            return {"error": g}
        if g is not None:
            nodes, edges = osm.process(g)
            db.write_graph_to_db(database, nodes, edges)

    # TODO: Next step - implement routing using the data
    return 'OK'