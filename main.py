import logging
import logging.config
import uvicorn
import config
import db
from db import connect, close, area_data
from api import create_app

def startup():
    # Set up logging and initialize resources.
    logging.config.dictConfig(config.LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info("Starting up application resources.")
    try:
        connect()
        logger.info("Database connection established.")
        db.initialize_indexes()
        logger.info("Database indexes created successfully.")
    except Exception as e:
        logger.error("Startup failed.", exc_info=e)
        raise e

def shutdown():
    # Execute shutdown routines, such as closing the db connection.
    logger = logging.getLogger(__name__)
    logger.info("Shutting down. Cleaning up resources.")
    close()

if __name__ == "__main__":
    try:
        startup()
        app = create_app()
        uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)
    finally:
        shutdown()