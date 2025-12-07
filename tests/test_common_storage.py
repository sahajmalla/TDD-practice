"""Common tests for all weather data storage functions using parametrization."""

import pytest
from src.tdd_practice.weather_storage import store_temperature
from src.tdd_practice.rainfall_storage import store_rainfall
from src.tdd_practice.wind_storage import store_wind_speed


@pytest.mark.parametrize("store_func,data_key,test_data", [
    (store_temperature, 'temperature', {'max': 10, 'min': 5, 'average': 7.5}),
    (store_rainfall, 'rainfall', 10.5),
    (store_wind_speed, 'wind_speed', {'min': 5.0, 'max': 15.0}),
])
def test_basic_storage(store_func, data_key, test_data):
    """Test basic storage functionality for all data types."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    
    store_func(date, hour, test_data, storage)
    
    assert date in storage
    assert hour in storage[date]
    assert storage[date][hour][data_key] == test_data


@pytest.mark.parametrize("store_func,data_key,test_data_list", [
    (store_temperature, 'temperature', [
        {'max': 5, 'min': 0, 'average': 2.5},
        {'max': 25, 'min': 15, 'average': 20},
        {'max': 10, 'min': 8, 'average': 9}
    ]),
    (store_rainfall, 'rainfall', [0.0, 5.5, 15.2]),
    (store_wind_speed, 'wind_speed', [
        {'min': 0.0, 'max': 5.0},
        {'min': 10.0, 'max': 25.0},
        {'min': 3.0, 'max': 8.0}
    ]),
])
def test_store_for_multiple_hours(store_func, data_key, test_data_list):
    """Test storing data for multiple hours."""
    date = '2024-01-15'
    storage = {}
    hours = [0, 12, 23]
    
    for hour, data in zip(hours, test_data_list):
        store_func(date, hour, data, storage)
    
    assert len(storage[date]) == 3
    for hour, expected_data in zip(hours, test_data_list):
        assert storage[date][hour][data_key] == expected_data


@pytest.mark.parametrize("store_func,data_key,initial_data,updated_data", [
    (store_temperature, 'temperature', 
     {'max': 10, 'min': 5, 'average': 7.5},
     {'max': 15, 'min': 8, 'average': 11.5}),
    (store_rainfall, 'rainfall', 5.0, 12.5),
    (store_wind_speed, 'wind_speed',
     {'min': 5.0, 'max': 10.0},
     {'min': 8.0, 'max': 20.0}),
])
def test_overwrites_existing(store_func, data_key, initial_data, updated_data):
    """Test that storing data for the same hour overwrites previous data."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    
    store_func(date, hour, initial_data, storage)
    store_func(date, hour, updated_data, storage)
    
    assert storage[date][hour][data_key] == updated_data
    assert storage[date][hour][data_key] != initial_data


@pytest.mark.parametrize("store_func,data_key,hour0_data,hour23_data", [
    (store_temperature, 'temperature',
     {'max': 5, 'min': 0, 'average': 2.5},
     {'max': 10, 'min': 5, 'average': 7.5}),
    (store_rainfall, 'rainfall', 2.5, 8.0),
    (store_wind_speed, 'wind_speed',
     {'min': 3.0, 'max': 8.0},
     {'min': 5.0, 'max': 12.0}),
])
def test_at_hour_boundaries(store_func, data_key, hour0_data, hour23_data):
    """Test storing data at hour boundaries (0 and 23)."""
    date = '2024-01-15'
    storage = {}
    
    store_func(date, 0, hour0_data, storage)
    store_func(date, 23, hour23_data, storage)
    
    assert 0 in storage[date]
    assert 23 in storage[date]
    assert storage[date][0][data_key] == hour0_data
    assert storage[date][23][data_key] == hour23_data


@pytest.mark.parametrize("store_func,invalid_hour", [
    (store_temperature, -1),
    (store_temperature, 24),
    (store_temperature, -10),
    (store_temperature, 100),
    (store_rainfall, -1),
    (store_rainfall, 24),
    (store_rainfall, -10),
    (store_rainfall, 100),
    (store_wind_speed, -1),
    (store_wind_speed, 24),
    (store_wind_speed, -10),
    (store_wind_speed, 100),
])
def test_fails_with_invalid_hour(store_func, invalid_hour):
    """Test that all storage functions fail with invalid hour values."""
    date = '2024-01-15'
    storage = {}
    
    # Create appropriate test data based on function
    if store_func == store_temperature:
        test_data = {'max': 10, 'min': 5, 'average': 7.5}
    elif store_func == store_rainfall:
        test_data = 10.5
    else:  # store_wind_speed
        test_data = {'min': 5.0, 'max': 15.0}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_func(date, invalid_hour, test_data, storage)


@pytest.mark.parametrize("store_func,data_key,test_data_list", [
    (store_temperature, 'temperature', [
        {'max': 20, 'min': 10, 'average': 15},
        {'max': 25, 'min': 15, 'average': 20},
        {'max': 18, 'min': 8, 'average': 13}
    ]),
    (store_rainfall, 'rainfall', [5.0, 12.5, 8.2]),
    (store_wind_speed, 'wind_speed', [
        {'min': 5.0, 'max': 15.0},
        {'min': 10.0, 'max': 25.0},
        {'min': 3.0, 'max': 8.0}
    ]),
])
def test_store_for_multiple_days(store_func, data_key, test_data_list):
    """Test storing data for multiple different days."""
    storage = {}
    dates = ['2024-01-15', '2024-01-16', '2024-01-17']
    hour = 10
    
    for date, data in zip(dates, test_data_list):
        store_func(date, hour, data, storage)
    
    assert len(storage) == 3
    for date, expected_data in zip(dates, test_data_list):
        assert date in storage
        assert storage[date][hour][data_key] == expected_data


@pytest.mark.parametrize("store_func,data_key,data1,data2", [
    (store_temperature, 'temperature',
     {'max': 20, 'min': 10, 'average': 15},
     {'max': 25, 'min': 15, 'average': 20}),
    (store_rainfall, 'rainfall', 5.0, 12.5),
    (store_wind_speed, 'wind_speed',
     {'min': 5.0, 'max': 15.0},
     {'min': 10.0, 'max': 25.0}),
])
def test_same_hour_different_days(store_func, data_key, data1, data2):
    """Test that storing data for the same hour on different days doesn't overwrite."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    hour = 10
    
    store_func(date1, hour, data1, storage)
    store_func(date2, hour, data2, storage)
    
    assert storage[date1][hour][data_key] == data1
    assert storage[date2][hour][data_key] == data2
    assert storage[date1][hour][data_key] != storage[date2][hour][data_key]

