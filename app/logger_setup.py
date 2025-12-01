import logging
import os

def configure_logger():
    # Create logs folder
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/weather_app.log"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger("weather_app")
    logger.debug("Logger initialized successfully")
    return logger