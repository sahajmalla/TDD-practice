"""Test cases for temperature data storage."""

import pytest
from src.tdd_practice.weather_storage import store_temperature


def test_store_temperature_data():
    """Test storing temperature data (max, min, average) for an hour."""
    date = '2024-01-15'
    hour = 10
    temperature_data = {
        'max': 10,
        'min': 5,
        'average': 7.5
    }
    storage = {}
    
    store_temperature(date, hour, temperature_data, storage)
    
    assert date in storage
    assert hour in storage[date]
    assert storage[date][hour]['temperature'] == {
        'max': 10,
        'min': 5,
        'average': 7.5
    }


def test_store_temperature_for_multiple_hours():
    """Test storing temperature data for multiple hours."""
    date = '2024-01-15'
    storage = {}
    hour1, hour2, hour3 = 0, 12, 23
    temp1 = {'max': 5, 'min': 0, 'average': 2.5}
    temp2 = {'max': 25, 'min': 15, 'average': 20}
    temp3 = {'max': 10, 'min': 8, 'average': 9}
    
    store_temperature(date, hour1, temp1, storage)
    store_temperature(date, hour2, temp2, storage)
    store_temperature(date, hour3, temp3, storage)
    
    assert len(storage[date]) == 3
    assert storage[date][hour1]['temperature'] == temp1
    assert storage[date][hour2]['temperature'] == temp2
    assert storage[date][hour3]['temperature'] == temp3


def test_store_temperature_overwrites_existing():
    """Test that storing temperature for the same hour overwrites previous data."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    initial_temp = {'max': 10, 'min': 5, 'average': 7.5}
    updated_temp = {'max': 15, 'min': 8, 'average': 11.5}
    
    store_temperature(date, hour, initial_temp, storage)
    store_temperature(date, hour, updated_temp, storage)
    
    assert storage[date][hour]['temperature'] == updated_temp
    assert storage[date][hour]['temperature'] != initial_temp


def test_store_temperature_with_negative_values():
    """Test storing temperature with negative values (valid for cold temperatures)."""
    date = '2024-01-15'
    hour = 10
    temperature_data = {
        'max': -5,
        'min': -10,
        'average': -7.5
    }
    storage = {}
    
    store_temperature(date, hour, temperature_data, storage)
    
    assert storage[date][hour]['temperature']['max'] == -5
    assert storage[date][hour]['temperature']['min'] == -10
    assert storage[date][hour]['temperature']['average'] == -7.5


def test_store_temperature_at_hour_boundaries():
    """Test storing temperature at hour boundaries (0 and 23)."""
    date = '2024-01-15'
    storage = {}
    hour0_temp = {'max': 5, 'min': 0, 'average': 2.5}
    hour23_temp = {'max': 10, 'min': 5, 'average': 7.5}
    
    store_temperature(date, 0, hour0_temp, storage)
    store_temperature(date, 23, hour23_temp, storage)
    
    assert 0 in storage[date]
    assert 23 in storage[date]
    assert storage[date][0]['temperature'] == hour0_temp
    assert storage[date][23]['temperature'] == hour23_temp


def test_store_temperature_fails_with_negative_hour():
    """Test that storing temperature fails when hour is negative."""
    date = '2024-01-15'
    hour = -1
    temperature_data = {'max': 10, 'min': 5, 'average': 7.5}
    storage = {}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_temperature(date, hour, temperature_data, storage)


def test_store_temperature_fails_with_hour_greater_than_23():
    """Test that storing temperature fails when hour is greater than 23."""
    date = '2024-01-15'
    hour = 24
    temperature_data = {'max': 10, 'min': 5, 'average': 7.5}
    storage = {}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_temperature(date, hour, temperature_data, storage)


def test_store_temperature_fails_with_hour_way_out_of_bounds():
    """Test that storing temperature fails with extremely out-of-bounds hour values."""
    date = '2024-01-15'
    storage = {}
    temperature_data = {'max': 10, 'min': 5, 'average': 7.5}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_temperature(date, -10, temperature_data, storage)
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_temperature(date, 100, temperature_data, storage)


def test_store_temperature_for_multiple_days():
    """Test storing temperature data for multiple different days."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    date3 = '2024-01-17'
    hour = 10
    temp1 = {'max': 20, 'min': 10, 'average': 15}
    temp2 = {'max': 25, 'min': 15, 'average': 20}
    temp3 = {'max': 18, 'min': 8, 'average': 13}
    
    store_temperature(date1, hour, temp1, storage)
    store_temperature(date2, hour, temp2, storage)
    store_temperature(date3, hour, temp3, storage)
    
    assert len(storage) == 3
    assert date1 in storage
    assert date2 in storage
    assert date3 in storage
    assert storage[date1][hour]['temperature'] == temp1
    assert storage[date2][hour]['temperature'] == temp2
    assert storage[date3][hour]['temperature'] == temp3


def test_store_temperature_same_hour_different_days():
    """Test that storing temperature for the same hour on different days doesn't overwrite."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    hour = 10
    temp1 = {'max': 20, 'min': 10, 'average': 15}
    temp2 = {'max': 25, 'min': 15, 'average': 20}
    
    store_temperature(date1, hour, temp1, storage)
    store_temperature(date2, hour, temp2, storage)
    
    assert storage[date1][hour]['temperature'] == temp1
    assert storage[date2][hour]['temperature'] == temp2
    assert storage[date1][hour]['temperature'] != storage[date2][hour]['temperature']
