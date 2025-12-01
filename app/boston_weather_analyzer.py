import logging

class WeatherAnalyzer:
    def __init__(self):
        self.logger = logging.getLogger("weather_app.analyzer")

    def average_temperature(self, df):
        self.logger.info("Calculating average temperature...")

        temp_col = df.columns[df.columns.str.contains("Max_TemperatureC", case=False)].tolist()

        if not temp_col:
            self.logger.error("Temperature column not found")
            raise KeyError("No temperature column detected")

        col = temp_col[0]
        avg_temp = df[col].mean()
        self.logger.debug(f"Average temperature from '{col}': {avg_temp}")
        return avg_temp

    def max_min_temperature(self, df):
        self.logger.info("Calculating maximum of minimum temperatures...")

        min_col = df.columns[df.columns.str.contains("Min_TemperatureC", case=False)].tolist()

        if not min_col:
            self.logger.error("Minimum temperature column not found")
            raise KeyError("No min temperature column detected")

        col = min_col[0]
        max_min_temp = df[col].max()
        self.logger.debug(f"Max of minimum temperatures from '{col}': {max_min_temp}")
        return max_min_temp

    def missing_values(self, df):
        self.logger.info("Checking for missing values...")
        missing = df.isna().sum()
        self.logger.debug(f"Missing values:\n{missing}")
        return missing