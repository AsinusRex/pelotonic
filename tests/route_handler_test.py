import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import api.route_handler as route_handler

# Dummy function for area_data.connect (Step 2)
def dummy_connect(origin, destination):
    # Assert format of origin and destination dictionaries
    assert isinstance(origin, dict)
    assert isinstance(destination, dict)
    assert "lat" in origin and "lon" in origin
    assert "lat" in destination and "lon" in destination
    # Return dummy tile IDs
    return ["tile1", "tile2", "tile3"]

# Dummy function for area_data.check (Step 3)
def dummy_check(tile_ids):
    # Assert that tile_ids is a list of strings
    assert isinstance(tile_ids, list)
    for tile in tile_ids:
        assert isinstance(tile, str)
    # Return a subset to simulate some existing tiles
    return ["tile1"]

# Dummy functions for data loading (Step 4)
def dummy_load_osm(tile):
    assert isinstance(tile, str)
def dummy_load_traffic(tile):
    assert isinstance(tile, str)
def dummy_load_weather(tile):
    assert isinstance(tile, str)

# Dummy function for optimization.calculate_weights (Step 6)
def dummy_calculate_weights(tiles, request_data):
    # Assert tiles is a list of strings
    assert isinstance(tiles, list)
    for tile in tiles:
        assert isinstance(tile, str)
    # Assert request_data contains the key "user_id"
    assert isinstance(request_data, dict)
    assert "user_id" in request_data
    # Return a dummy weights object
    return {"dummy_weight": 1}

# Dummy function for route.plot (Step 7)
def dummy_plot(tiles, weights):
    # Assert tiles is a list and weights is a dictionary
    assert isinstance(tiles, list)
    assert isinstance(weights, dict)
    # Return a dummy final route string
    return "dummy final route"

# Setup test FastAPI app with the router
app = FastAPI()
app.include_router(route_handler.router)
client = TestClient(app)

def test_route_handler_data_flow(monkeypatch):
    # Monkeypatch external functions for each step

    # Step 2
    monkeypatch.setattr(route_handler.area_data, "connect", dummy_connect)
    # Step 3
    monkeypatch.setattr(route_handler.area_data, "check", dummy_check)
    # Step 4: Stub the loading functions
    monkeypatch.setattr(route_handler.area_data, "load_osm", dummy_load_osm)
    monkeypatch.setattr(route_handler.area_data, "load_traffic", dummy_load_traffic)
    monkeypatch.setattr(route_handler.area_data, "load_weather", dummy_load_weather)
    # Step 6
    monkeypatch.setattr(route_handler.optimization, "calculate_weights", dummy_calculate_weights)
    # Step 7
    monkeypatch.setattr(route_handler.route, "plot", dummy_plot)

    # Setup query parameters for a valid request
    params = {
        "origin_lat": 41.4723,
        "origin_lon": 2.0861,
        "dest_lat": 41.3851,
        "dest_lon": 2.1734,
        "user_id": "testuser"
    }

    response = client.get("/route", params=params)
    assert response.status_code == 200
    data = response.json()
    # Assert that final route is in expected format
    assert "route" in data
    assert data["route"] == "dummy final route"

def test_invalid_format(monkeypatch):
    # Monkeypatch only the functions that are not expected to be reached
    monkeypatch.setattr(route_handler.area_data, "connect", dummy_connect)
    monkeypatch.setattr(route_handler.area_data, "check", dummy_check)
    monkeypatch.setattr(route_handler.area_data, "load_osm", dummy_load_osm)
    monkeypatch.setattr(route_handler.area_data, "load_traffic", dummy_load_traffic)
    monkeypatch.setattr(route_handler.area_data, "load_weather", dummy_load_weather)
    monkeypatch.setattr(route_handler.optimization, "calculate_weights", dummy_calculate_weights)
    monkeypatch.setattr(route_handler.route, "plot", dummy_plot)

    # Missing one of the required query parameters to check validation (Step 1)
    params = {
        "origin_lat": 41.4723,
        "origin_lon": 2.0861,
        # "dest_lat" is missing
        "dest_lon": 2.1734,
        "user_id": "testuser"
    }
    response = client.get("/route", params=params)
    # FastAPI raises a 422 error for missing required query param
    assert response.status_code == 422