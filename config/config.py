import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)

def load_config():
    """
    Loads configuration from environment variables or defaults.
    """
    logging.info("Loading configuration from environment...")
    load_dotenv()

    config = {
        "MONGO_URI": os.getenv("MONGO_URI", "mongodb://localhost:27017/"),
        "DB_NAME": os.getenv("DB_NAME", "bike_routing"),
        "API_HOST": os.getenv("API_HOST", "0.0.0.0"),
        "API_PORT": int(os.getenv("API_PORT", "8000")),
        "SEARCH_RADIUS_METERS": int(os.getenv("SEARCH_RADIUS_METERS", "10000")),
        "SEARCH_GRID_METERS": int(os.getenv("SEARCH_GRID_METERS", "1000")),
        "LOGGING_CONFIG": {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
                },
            },
            "handlers": {
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "": {"handlers": ["default"], "level": "INFO"},
                "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
                "uvicorn.error": {"handlers": ["default"], "level": "INFO", "propagate": False},
                "uvicorn.access": {"handlers": ["default"], "level": "INFO", "propagate": False},
            },
        }
    }

    logging.info("Configuration loaded: %s", config)
    return config
