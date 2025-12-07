"""Wind speed storage functions for hourly min and max wind speed values."""


def store_wind_speed(date: str, hour: int, wind_speed_data: dict, storage: dict) -> None:
    """
    Store wind speed data for a specific date and hour.
    
    Args:
        date: The date in format 'YYYY-MM-DD' (e.g., '2024-01-15')
        hour: The hour (0-23) for which to store wind speed data
        wind_speed_data: Dictionary containing 'min' and 'max' wind speed values
        storage: Dictionary to store the weather data, organized by date and hour
    
    Raises:
        ValueError: If hour is not in the valid range (0-23)
    """
    if hour < 0 or hour > 23:
        raise ValueError(f"Hour must be between 0 and 23, got {hour}")
    if date not in storage:
        storage[date] = {}
    if hour not in storage[date]:
        storage[date][hour] = {}
    storage[date][hour]['wind_speed'] = wind_speed_data

