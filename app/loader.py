import pandas as pd
import logging

class WeatherDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = logging.getLogger("weather_app.loader")

    def load(self):
        self.logger.info(f"Loading dataset from {self.file_path}")

        try:
            df = pd.read_csv(self.file_path)
            self.logger.debug(f"Dataset loaded successfully with shape {df.shape}")
            return df
        
        except FileNotFoundError:
            self.logger.exception("Dataset file not found")
            raise
        
        except Exception:
            self.logger.exception("Unexpected error while loading dataset")
            raise