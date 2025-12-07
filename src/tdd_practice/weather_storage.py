"""Weather data storage functions for hourly temperature, rainfall, and wind speed."""


def store_temperature(date: str, hour: int, temperature_data: dict, storage: dict) -> None:
    """
    Store temperature data for a specific date and hour.
    
    Args:
        date: The date in format 'YYYY-MM-DD' (e.g., '2024-01-15')
        hour: The hour (0-23) for which to store temperature data
        temperature_data: Dictionary containing 'max', 'min', and 'average' temperature values
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
    storage[date][hour]['temperature'] = temperature_data

