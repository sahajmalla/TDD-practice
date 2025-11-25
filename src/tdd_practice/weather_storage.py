"""Weather data storage functions for hourly temperature, rainfall, and wind speed."""


def store_temperature(hour: int, temperature_data: dict, storage: dict) -> None:
    """
    Store temperature data for a specific hour.
    
    Args:
        hour: The hour (0-23) for which to store temperature data
        temperature_data: Dictionary containing 'max', 'min', and 'average' temperature values
        storage: Dictionary to store the weather data, organized by hour
    """
    if hour not in storage:
        storage[hour] = {}
    storage[hour]['temperature'] = temperature_data

