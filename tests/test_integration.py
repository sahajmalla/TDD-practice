"""Integration tests for storing all weather data types together."""

from src.tdd_practice.weather_storage import store_temperature
from src.tdd_practice.rainfall_storage import store_rainfall
from src.tdd_practice.wind_storage import store_wind_speed


def test_store_all_data_types_for_same_hour():
    """Test storing temperature, rainfall, and wind speed for the same hour."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    temperature_data = {'max': 25, 'min': 15, 'average': 20}
    rainfall_value = 5.5
    wind_speed_data = {'min': 5.0, 'max': 15.0}
    
    store_temperature(date, hour, temperature_data, storage)
    store_rainfall(date, hour, rainfall_value, storage)
    store_wind_speed(date, hour, wind_speed_data, storage)
    
    assert date in storage
    assert hour in storage[date]
    assert 'temperature' in storage[date][hour]
    assert 'rainfall' in storage[date][hour]
    assert 'wind_speed' in storage[date][hour]
    assert storage[date][hour]['temperature'] == temperature_data
    assert storage[date][hour]['rainfall'] == rainfall_value
    assert storage[date][hour]['wind_speed'] == wind_speed_data


def test_independent_data_source_updates():
    """Test that different data sources can update independently without affecting others."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    initial_temp = {'max': 20, 'min': 10, 'average': 15}
    initial_rainfall = 5.0
    initial_wind = {'min': 5.0, 'max': 10.0}
    
    store_temperature(date, hour, initial_temp, storage)
    store_rainfall(date, hour, initial_rainfall, storage)
    store_wind_speed(date, hour, initial_wind, storage)
    
    # Update only temperature (from control center)
    updated_temp = {'max': 25, 'min': 15, 'average': 20}
    store_temperature(date, hour, updated_temp, storage)
    
    assert storage[date][hour]['temperature'] == updated_temp
    assert storage[date][hour]['rainfall'] == initial_rainfall
    assert storage[date][hour]['wind_speed'] == initial_wind
    
    # Update only rainfall (from sensor)
    updated_rainfall = 12.5
    store_rainfall(date, hour, updated_rainfall, storage)
    
    assert storage[date][hour]['temperature'] == updated_temp
    assert storage[date][hour]['rainfall'] == updated_rainfall
    assert storage[date][hour]['wind_speed'] == initial_wind
    
    # Update only wind speed (from sensor)
    updated_wind = {'min': 10.0, 'max': 20.0}
    store_wind_speed(date, hour, updated_wind, storage)
    
    assert storage[date][hour]['temperature'] == updated_temp
    assert storage[date][hour]['rainfall'] == updated_rainfall
    assert storage[date][hour]['wind_speed'] == updated_wind


def test_store_data_for_multiple_hours_with_all_types():
    """Test storing all data types for multiple different hours."""
    date = '2024-01-15'
    storage = {}
    hour1, hour2, hour3 = 0, 12, 23
    
    store_temperature(date, hour1, {'max': 5, 'min': 0, 'average': 2.5}, storage)
    store_rainfall(date, hour1, 0.0, storage)
    store_wind_speed(date, hour1, {'min': 2.0, 'max': 5.0}, storage)
    
    store_temperature(date, hour2, {'max': 25, 'min': 15, 'average': 20}, storage)
    store_rainfall(date, hour2, 10.5, storage)
    store_wind_speed(date, hour2, {'min': 10.0, 'max': 25.0}, storage)
    
    store_temperature(date, hour3, {'max': 10, 'min': 5, 'average': 7.5}, storage)
    store_rainfall(date, hour3, 3.2, storage)
    store_wind_speed(date, hour3, {'min': 5.0, 'max': 12.0}, storage)
    
    assert len(storage[date]) == 3
    for hour in [hour1, hour2, hour3]:
        assert 'temperature' in storage[date][hour]
        assert 'rainfall' in storage[date][hour]
        assert 'wind_speed' in storage[date][hour]


def test_partial_data_storage():
    """Test storing data incrementally - temperature first, then add rainfall and wind."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    
    store_temperature(date, hour, {'max': 20, 'min': 10, 'average': 15}, storage)
    
    assert 'temperature' in storage[date][hour]
    assert 'rainfall' not in storage[date][hour]
    assert 'wind_speed' not in storage[date][hour]
    
    store_rainfall(date, hour, 5.5, storage)
    
    assert 'temperature' in storage[date][hour]
    assert 'rainfall' in storage[date][hour]
    assert storage[date][hour]['temperature'] == {'max': 20, 'min': 10, 'average': 15}
    assert storage[date][hour]['rainfall'] == 5.5
    
    store_wind_speed(date, hour, {'min': 5.0, 'max': 10.0}, storage)
    
    assert 'temperature' in storage[date][hour]
    assert 'rainfall' in storage[date][hour]
    assert 'wind_speed' in storage[date][hour]
    assert storage[date][hour]['temperature'] == {'max': 20, 'min': 10, 'average': 15}
    assert storage[date][hour]['rainfall'] == 5.5
    assert storage[date][hour]['wind_speed'] == {'min': 5.0, 'max': 10.0}


def test_store_data_for_multiple_days():
    """Test storing all data types for multiple different days."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    date3 = '2024-01-17'
    hour = 10
    
    store_temperature(date1, hour, {'max': 20, 'min': 10, 'average': 15}, storage)
    store_rainfall(date1, hour, 5.0, storage)
    store_wind_speed(date1, hour, {'min': 5.0, 'max': 15.0}, storage)
    
    store_temperature(date2, hour, {'max': 25, 'min': 15, 'average': 20}, storage)
    store_rainfall(date2, hour, 12.5, storage)
    store_wind_speed(date2, hour, {'min': 10.0, 'max': 25.0}, storage)
    
    store_temperature(date3, hour, {'max': 18, 'min': 8, 'average': 13}, storage)
    store_rainfall(date3, hour, 3.2, storage)
    store_wind_speed(date3, hour, {'min': 3.0, 'max': 8.0}, storage)
    
    assert len(storage) == 3
    for date in [date1, date2, date3]:
        assert date in storage
        assert 'temperature' in storage[date][hour]
        assert 'rainfall' in storage[date][hour]
        assert 'wind_speed' in storage[date][hour]


def test_same_hour_different_days_independent():
    """Test that storing data for the same hour on different days doesn't interfere."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    hour = 10
    
    store_temperature(date1, hour, {'max': 20, 'min': 10, 'average': 15}, storage)
    store_rainfall(date1, hour, 5.0, storage)
    store_wind_speed(date1, hour, {'min': 5.0, 'max': 15.0}, storage)
    
    store_temperature(date2, hour, {'max': 25, 'min': 15, 'average': 20}, storage)
    store_rainfall(date2, hour, 12.5, storage)
    store_wind_speed(date2, hour, {'min': 10.0, 'max': 25.0}, storage)
    
    assert storage[date1][hour]['temperature'] == {'max': 20, 'min': 10, 'average': 15}
    assert storage[date1][hour]['rainfall'] == 5.0
    assert storage[date1][hour]['wind_speed'] == {'min': 5.0, 'max': 15.0}
    
    assert storage[date2][hour]['temperature'] == {'max': 25, 'min': 15, 'average': 20}
    assert storage[date2][hour]['rainfall'] == 12.5
    assert storage[date2][hour]['wind_speed'] == {'min': 10.0, 'max': 25.0}
    
    # Verify they don't interfere with each other
    assert storage[date1][hour]['temperature'] != storage[date2][hour]['temperature']
    assert storage[date1][hour]['rainfall'] != storage[date2][hour]['rainfall']
    assert storage[date1][hour]['wind_speed'] != storage[date2][hour]['wind_speed']
