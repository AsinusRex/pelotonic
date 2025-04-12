# python
import logging
from pymongo import MongoClient, GEOSPHERE
import config

_db_client = None
_client = None
logger = logging.getLogger(__name__)

def connect():
    global _client, _db_client
    if _db_client is None:
        try:
            # Temporary client for a quick ping check with short timeouts
            tmp_client = MongoClient(
                config.MONGO_URI,
                socketTimeoutMS=500,
                connectTimeoutMS=500,
                serverSelectionTimeoutMS=500
            )
            tmp_client.admin.command('ping')
            # Create the main client without the limited timeouts for normal operations
            client = MongoClient(config.MONGO_URI)
            _db_client = client[config.DB_NAME]
            _client = client
        except Exception as error:
            print(f"Error connecting to MongoDB: {error}")
            raise
    return _db_client

def close():
    global _client, _db_client
    if _client:
        _client.close()
        logger.info("MongoDB connection closed gracefully.")
    _client = None
    _db_client = None

from . import area_data, user_data


def initialize_indexes():
    """
     Initializes indexes on the tiles collection for optimal query performance.

     Indexes to be created:
       1. The primary key index on the '_id' field is auto-created by MongoDB.
       2. A geospatial index (2dsphere) on the 'tile_polygon' field:
          - This index allows efficient geospatial queries (e.g., determining which tile contains a given coordinate).
          - The 'tile_polygon' field is expected to store a GeoJSON Polygon representing the tile's boundaries.

     Implementation steps:
       - Retrieve the global MongoDB connection (created by connect()).
       - Access the 'tiles' collection.
       - Use the collection's create_index() method to create a 2dsphere index on the 'tile_polygon' field.
       - Handle any exceptions that may occur during index creation and raise errors as needed.
     """
    try:
        tiles_collection = _db_client["tiles"]
        tiles_collection.create_index([("tile_polygon", GEOSPHERE)])
    except Exception as e:
        print(f"Error creating index: {e}")
        raise