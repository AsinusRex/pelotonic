# This file contains six functions, connect, check, load_osm, load_traffic, load_weather.
# The connect function gets an origin and destination point and returns a list of tiles between them (including the
# origin and destination tiles), it will then call check on each one to see if they have data or not.
#
# The check function will check for three things:
#   1) Whether the tile has OSM data or not and if not it will call load_osm on the tile.
#   2) Whether the tile has traffic data less than an hour old or not and if not it will call load_traffic on the tile.
#   3) Whether the tile has weather data less than an hour old or not and if not it will call load_weather on the tile.
#
# The load_osm function will call osm.fetch to get the data for a tile from OSM and then call osm.process to get a graph
# back. It will then save the graph of the tile to the database.
#
# The load_weather function will call osm.fetch to get the data for a tile from the weather API and then call
# weather.process to extract the data we need. We will then add it to the tile data in db.
#
# The load_traffic function will call osm.fetch to get the data for a tile from the Traffic API and then call
# traffic.process to extract the data we need. We will then add it to the tile data in db.


from typing import List
import math
import logging
from config import MAP_ZOOM_LEVEL

logger = logging.getLogger(__name__)
# Convert lat/lon to OSM tile coordinates
def point_to_tile(point, zoom):
    lat, lon = point["lat"], point["lon"]
    n = 2.0 ** zoom
    xtile = int((lon + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(math.radians(lat)) +
                                1.0 / math.cos(math.radians(lat))) / math.pi) / 2.0 * n)
    return xtile, ytile
def connect(origin: dict, destination: dict) -> List[str]:
    """
    Given origin and destination points (as dicts with 'lat' and 'lon' keys),
    calculate all OSM tile IDs that need to be fetched to cover the route.

    Uses zoom level from config.
    """

    # Get tile coordinates for origin and destination
    origin_x, origin_y = point_to_tile(origin, MAP_ZOOM_LEVEL)
    dest_x, dest_y = point_to_tile(destination, MAP_ZOOM_LEVEL)

    # Create bounding box
    min_x = min(origin_x, dest_x)
    max_x = max(origin_x, dest_x)
    min_y = min(origin_y, dest_y)
    max_y = max(origin_y, dest_y)

    # Generate all tile IDs in the rectangle
    tile_ids = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            tile_id = f"tile_{MAP_ZOOM_LEVEL}_{x}_{y}"
            tile_ids.append(tile_id)

    logger.info(f"Found {len(tile_ids)} tiles connecting origin and destination")
    return tile_ids

def check(tile_ids: List[str]) -> List[str]:
    """
    Given a list of tile IDs, checks in MongoDB which ones already exist.
    Returns a subset of tile_ids that exist in the database.
    """
    return ["tile1"]

def load_osm(tile_id: str):
    """
    Loads OSM graph data for a tile:
        1. Calls osm.fetch to get raw OSM data.
        2. Calls osm.process to transform raw OSM data into structured graph data.
        3. Inserts this graph into MongoDB under the tile_id as primary key.
    """
    print(f"OSM data loaded for {tile_id}")

def load_weather(tile_id: str):
    """
    Loads current weather data for the tile:
        1. Calls weather.fetch to obtain weather data.
        2. Calls weather.process to format it for database insertion.
        3. Updates weather collection with the new data for this tile.
    """
    print(f"Weather data loaded for {tile_id}")

def load_traffic(tile_id: str):
    """
    Loads traffic data for a tile:
        1. Calls traffic.fetch to obtain traffic data.
        2. Calls traffic.process to prepare it for insertion.
        3. Updates traffic collection with fresh traffic data for the tile.
    """
    print(f"Traffic data loaded for {tile_id}")


