# This file will call on the openmeteo API to get weather data for a specific tile and return it.
#  The URL is in the config and there is a library to handle requests to it. Sample use:
#
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
# 	"latitude": 52.52,
# 	"longitude": 13.41,
# 	"hourly": "temperature_2m"
# }
# responses = openmeteo.weather_api(url, params=params).

def fetch(tile_id: str):
    """
    Fetches weather data for a tile from OpenMeteo:
        1. Converts tile_id into coordinates (e.g., tile center).
        2. Queries OpenMeteo API using coordinates and WEATHER_API_KEY from config.
        3. Returns raw weather data for the tile.
    """
    pass