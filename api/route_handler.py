# Language: python
from fastapi import APIRouter, HTTPException, Query
import logging
import db.area_data as area_data
import optimization
import route

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/route")
def get_route(
        origin_lat: float = Query(...),
        origin_lon: float = Query(...),
        dest_lat: float = Query(...),
        dest_lon: float = Query(...),
        user_id: str = Query(...)
):
    """
    Handles a client's route request using query parameters.
    """
    origin = {"lat": origin_lat, "lon": origin_lon}
    destination = {"lat": dest_lat, "lon": dest_lon}
    logger.info(f"Step 1: Received origin {origin} and destination {destination}.")

    tile_ids = area_data.connect(origin, destination)
    logger.info(f"Step 2: Connected tiles calculated: {tile_ids}")

    existing_tiles = area_data.check(tile_ids)
    logger.info(f"Step 3: Existing tiles in the database: {existing_tiles}")

    missing_tiles = [tile for tile in tile_ids if tile not in existing_tiles]
    logger.info(f"Step 4: Missing tiles that need data loading: {missing_tiles}")
    for tile in missing_tiles:
        area_data.load_osm(tile)
        logger.info(f"Loaded OSM data for tile {tile}")
        area_data.load_traffic(tile)
        logger.info(f"Loaded traffic data for tile {tile}")
        area_data.load_weather(tile)
        logger.info(f"Loaded weather data for tile {tile}")

    tiles_data = tile_ids
    logger.info(f"Step 5: Tile data prepared for updating: {tiles_data}")

    # For example, you can add extra data to simulate the request body
    request_data = {"user_id": user_id}
    weights = optimization.calculate_weights(tiles_data, request_data)
    logger.info("Step 6: Edge weights updated.")

    final_route = route.plot(tiles_data, weights)
    logger.info(f"Step 7: Final route calculated: {final_route}")

    return {"route": final_route}