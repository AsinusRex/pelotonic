import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "bike_routing")
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
SEARCH_RADIUS_METERS = int(os.getenv("SEARCH_RADIUS_METERS", "10000"))
SEARCH_GRID_METERS = int(os.getenv("SEARCH_GRID_METERS", "1000"))
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "x")
WEATHER_API_URL = os.getenv("WEATHER_API_URL", "https://api.open-meteo.com/v1/forecast")
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY", "x")
TOMTOM_API_URL = os.getenv("TOMTOM_API_URL", "https://api.tomtom.com/")
WEATHER_DATA_MAX_AGE_MINUTES = int(os.getenv("WEATHER_DATA_MAX_AGE_MINUTES", "60"))
TRAFFIC_DATA_MAX_AGE_MINUTES = int(os.getenv("TRAFFIC_DATA_MAX_AGE_MINUTES", "60")),
MAP_ZOOM_LEVEL = int(os.getenv("MAP_ZOOM_LEVEL", "16"))
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}
