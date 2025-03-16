import logging.config  # <-- needed to use dictConfig
import uvicorn
from db import db
from api.server import app
from config.config import load_config

def init_app():
    # Load your custom config
    config = load_config()

    # Apply logging configuration
    logging.config.dictConfig(config["LOGGING_CONFIG"])

    logging.info("Initializing app...")
    database = db.connect(config.get("MONGO_URI"), config.get("DB_NAME"))

    if database is None:
        logging.error("MongoDB connection failed during initialization.")
        raise Exception("MongoDB connection failed.")

    # Store the db instance in the app state
    app.state.db = database

    logging.info("Starting API server at %s:%d", config.get("API_HOST"), config.get("API_PORT"))

    # Run Uvicorn with your custom logging configuration
    uvicorn.run(
        app,
        host=config.get("API_HOST"),
        port=config.get("API_PORT"),
        log_config=config["LOGGING_CONFIG"]
    )

if __name__ == "__main__":
    init_app()
