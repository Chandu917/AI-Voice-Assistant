def handle(tokens):
    if "weather" in tokens:
        print("Weather plugin triggered.")
        return "It looks sunny today!"
    return None

def get_detailed_forecast(location):
    """Add detailed weather forecast with precipitation chance"""
    # Implementation using OpenWeatherMap API