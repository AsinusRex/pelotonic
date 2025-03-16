from fastapi import FastAPI, Request
from api import route_handler
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/route")
def route_request(origin_lat: float, origin_lon: float,
                  dest_lat: float, dest_lon: float, user_id: str,
                  request: Request):
    # Retrieve the db instance from the app state
    db = request.app.state.db

    # Pass the db instance to your orchestrate_request function
    return route_handler.orchestrate_request(
        origin_lat, origin_lon, dest_lat, dest_lon, user_id)