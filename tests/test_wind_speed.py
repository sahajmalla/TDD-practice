"""Test cases for wind speed data storage."""

import pytest
from src.tdd_practice.wind_storage import store_wind_speed


def test_store_wind_speed_data():
    """Test storing wind speed data (min, max) for an hour."""
    date = '2024-01-15'
    hour = 10
    wind_speed_data = {
        'min': 5.0,
        'max': 15.0
    }
    storage = {}
    
    store_wind_speed(date, hour, wind_speed_data, storage)
    
    assert date in storage
    assert hour in storage[date]
    assert storage[date][hour]['wind_speed'] == {
        'min': 5.0,
        'max': 15.0
    }


def test_store_wind_speed_for_multiple_hours():
    """Test storing wind speed data for multiple hours."""
    date = '2024-01-15'
    storage = {}
    hour1, hour2, hour3 = 0, 12, 23
    wind1 = {'min': 0.0, 'max': 5.0}
    wind2 = {'min': 10.0, 'max': 25.0}
    wind3 = {'min': 3.0, 'max': 8.0}
    
    store_wind_speed(date, hour1, wind1, storage)
    store_wind_speed(date, hour2, wind2, storage)
    store_wind_speed(date, hour3, wind3, storage)
    
    assert len(storage[date]) == 3
    assert storage[date][hour1]['wind_speed'] == wind1
    assert storage[date][hour2]['wind_speed'] == wind2
    assert storage[date][hour3]['wind_speed'] == wind3


def test_store_wind_speed_overwrites_existing():
    """Test that storing wind speed for the same hour overwrites previous data."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    initial_wind = {'min': 5.0, 'max': 10.0}
    updated_wind = {'min': 8.0, 'max': 20.0}
    
    store_wind_speed(date, hour, initial_wind, storage)
    store_wind_speed(date, hour, updated_wind, storage)
    
    assert storage[date][hour]['wind_speed'] == updated_wind
    assert storage[date][hour]['wind_speed'] != initial_wind


def test_store_wind_speed_zero_values():
    """Test storing wind speed with zero min value (calm conditions)."""
    date = '2024-01-15'
    hour = 10
    wind_speed_data = {
        'min': 0.0,
        'max': 2.0
    }
    storage = {}
    
    store_wind_speed(date, hour, wind_speed_data, storage)
    
    assert storage[date][hour]['wind_speed']['min'] == 0.0
    assert storage[date][hour]['wind_speed']['max'] == 2.0


def test_store_wind_speed_at_hour_boundaries():
    """Test storing wind speed at hour boundaries (0 and 23)."""
    date = '2024-01-15'
    storage = {}
    hour0_wind = {'min': 3.0, 'max': 8.0}
    hour23_wind = {'min': 5.0, 'max': 12.0}
    
    store_wind_speed(date, 0, hour0_wind, storage)
    store_wind_speed(date, 23, hour23_wind, storage)
    
    assert 0 in storage[date]
    assert 23 in storage[date]
    assert storage[date][0]['wind_speed'] == hour0_wind
    assert storage[date][23]['wind_speed'] == hour23_wind


def test_store_wind_speed_high_values():
    """Test storing high wind speed values (strong winds)."""
    date = '2024-01-15'
    hour = 10
    wind_speed_data = {
        'min': 30.0,
        'max': 50.0
    }
    storage = {}
    
    store_wind_speed(date, hour, wind_speed_data, storage)
    
    assert storage[date][hour]['wind_speed']['min'] == 30.0
    assert storage[date][hour]['wind_speed']['max'] == 50.0


def test_store_wind_speed_fails_with_negative_hour():
    """Test that storing wind speed fails when hour is negative."""
    date = '2024-01-15'
    hour = -1
    wind_speed_data = {'min': 5.0, 'max': 15.0}
    storage = {}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_wind_speed(date, hour, wind_speed_data, storage)


def test_store_wind_speed_fails_with_hour_greater_than_23():
    """Test that storing wind speed fails when hour is greater than 23."""
    date = '2024-01-15'
    hour = 24
    wind_speed_data = {'min': 5.0, 'max': 15.0}
    storage = {}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_wind_speed(date, hour, wind_speed_data, storage)


def test_store_wind_speed_fails_with_hour_way_out_of_bounds():
    """Test that storing wind speed fails with extremely out-of-bounds hour values."""
    date = '2024-01-15'
    storage = {}
    wind_speed_data = {'min': 5.0, 'max': 15.0}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_wind_speed(date, -10, wind_speed_data, storage)
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_wind_speed(date, 100, wind_speed_data, storage)


def test_store_wind_speed_for_multiple_days():
    """Test storing wind speed data for multiple different days."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    date3 = '2024-01-17'
    hour = 10
    wind1 = {'min': 5.0, 'max': 15.0}
    wind2 = {'min': 10.0, 'max': 25.0}
    wind3 = {'min': 3.0, 'max': 8.0}
    
    store_wind_speed(date1, hour, wind1, storage)
    store_wind_speed(date2, hour, wind2, storage)
    store_wind_speed(date3, hour, wind3, storage)
    
    assert len(storage) == 3
    assert date1 in storage
    assert date2 in storage
    assert date3 in storage
    assert storage[date1][hour]['wind_speed'] == wind1
    assert storage[date2][hour]['wind_speed'] == wind2
    assert storage[date3][hour]['wind_speed'] == wind3


def test_store_wind_speed_same_hour_different_days():
    """Test that storing wind speed for the same hour on different days doesn't overwrite."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    hour = 10
    wind1 = {'min': 5.0, 'max': 15.0}
    wind2 = {'min': 10.0, 'max': 25.0}
    
    store_wind_speed(date1, hour, wind1, storage)
    store_wind_speed(date2, hour, wind2, storage)
    
    assert storage[date1][hour]['wind_speed'] == wind1
    assert storage[date2][hour]['wind_speed'] == wind2
    assert storage[date1][hour]['wind_speed'] != storage[date2][hour]['wind_speed']
