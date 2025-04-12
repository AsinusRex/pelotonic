# This file has a function to fetch traffic data for the tile it receives and returns it.
# The url is in the config and the path is traffic/services/{versionNumber}/flowSegmentData/{style}/{zoom}/{format}.

def fetch(tile_id: str):
    """
    Fetches traffic data for a tile from TomTom Traffic API:
        1. Converts tile_id to appropriate URL parameters.
        2. Sends request to TomTom Traffic API with configured credentials.
        3. Returns raw traffic data.
    """
    pass

