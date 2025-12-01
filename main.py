from app.logger_setup import configure_logger
from app.loader import WeatherDataLoader
from app.weather_analyzer import WeatherAnalyzer

def main():
    logger = configure_logger()
    logger.info("Weather analysis application started")

    loader = WeatherDataLoader("data/weather_data.csv")
    df = loader.load()

    analyzer = WeatherAnalyzer()

    avg_temp = analyzer.average_temperature(df)
    logger.info(f"Average Temperature: {avg_temp}")

    max_min_temp = analyzer.max_min_temperature(df)
    logger.info(f"Maximum of Minimum Temperatures: {max_min_temp}")

    missing = analyzer.missing_values(df)
    logger.info("Missing Values Report Generated")

    logger.info("Application finished successfully")

if __name__ == "__main__":
    main()