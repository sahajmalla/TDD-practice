"""Test cases for rainfall data storage."""

import pytest
from src.tdd_practice.rainfall_storage import store_rainfall


def test_store_rainfall_value():
    """Test storing rainfall value for an hour."""
    date = '2024-01-15'
    hour = 10
    rainfall_value = 10.5
    storage = {}
    
    store_rainfall(date, hour, rainfall_value, storage)
    
    assert date in storage
    assert hour in storage[date]
    assert storage[date][hour]['rainfall'] == 10.5


def test_store_rainfall_for_multiple_hours():
    """Test storing rainfall data for multiple hours."""
    date = '2024-01-15'
    storage = {}
    hour1, hour2, hour3 = 0, 12, 23
    rainfall1, rainfall2, rainfall3 = 0.0, 5.5, 15.2
    
    store_rainfall(date, hour1, rainfall1, storage)
    store_rainfall(date, hour2, rainfall2, storage)
    store_rainfall(date, hour3, rainfall3, storage)
    
    assert len(storage[date]) == 3
    assert storage[date][hour1]['rainfall'] == 0.0
    assert storage[date][hour2]['rainfall'] == 5.5
    assert storage[date][hour3]['rainfall'] == 15.2


def test_store_rainfall_overwrites_existing():
    """Test that storing rainfall for the same hour overwrites previous data."""
    date = '2024-01-15'
    hour = 10
    storage = {}
    initial_rainfall = 5.0
    updated_rainfall = 12.5
    
    store_rainfall(date, hour, initial_rainfall, storage)
    store_rainfall(date, hour, updated_rainfall, storage)
    
    assert storage[date][hour]['rainfall'] == updated_rainfall
    assert storage[date][hour]['rainfall'] != initial_rainfall


def test_store_rainfall_zero_value():
    """Test storing zero rainfall (no rain)."""
    date = '2024-01-15'
    hour = 10
    rainfall_value = 0.0
    storage = {}
    
    store_rainfall(date, hour, rainfall_value, storage)
    
    assert storage[date][hour]['rainfall'] == 0.0


def test_store_rainfall_at_hour_boundaries():
    """Test storing rainfall at hour boundaries (0 and 23)."""
    date = '2024-01-15'
    storage = {}
    hour0_rainfall = 2.5
    hour23_rainfall = 8.0
    
    store_rainfall(date, 0, hour0_rainfall, storage)
    store_rainfall(date, 23, hour23_rainfall, storage)
    
    assert 0 in storage[date]
    assert 23 in storage[date]
    assert storage[date][0]['rainfall'] == hour0_rainfall
    assert storage[date][23]['rainfall'] == hour23_rainfall


def test_store_rainfall_high_value():
    """Test storing high rainfall values (heavy rain)."""
    date = '2024-01-15'
    hour = 10
    rainfall_value = 50.5
    storage = {}
    
    store_rainfall(date, hour, rainfall_value, storage)
    
    assert storage[date][hour]['rainfall'] == 50.5


def test_store_rainfall_fails_with_negative_hour():
    """Test that storing rainfall fails when hour is negative."""
    date = '2024-01-15'
    hour = -1
    rainfall_value = 10.5
    storage = {}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_rainfall(date, hour, rainfall_value, storage)


def test_store_rainfall_fails_with_hour_greater_than_23():
    """Test that storing rainfall fails when hour is greater than 23."""
    date = '2024-01-15'
    hour = 24
    rainfall_value = 10.5
    storage = {}
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_rainfall(date, hour, rainfall_value, storage)


def test_store_rainfall_fails_with_hour_way_out_of_bounds():
    """Test that storing rainfall fails with extremely out-of-bounds hour values."""
    date = '2024-01-15'
    storage = {}
    rainfall_value = 10.5
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_rainfall(date, -10, rainfall_value, storage)
    
    with pytest.raises(ValueError, match="Hour must be between 0 and 23"):
        store_rainfall(date, 100, rainfall_value, storage)


def test_store_rainfall_for_multiple_days():
    """Test storing rainfall data for multiple different days."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    date3 = '2024-01-17'
    hour = 10
    rainfall1, rainfall2, rainfall3 = 5.0, 12.5, 8.2
    
    store_rainfall(date1, hour, rainfall1, storage)
    store_rainfall(date2, hour, rainfall2, storage)
    store_rainfall(date3, hour, rainfall3, storage)
    
    assert len(storage) == 3
    assert date1 in storage
    assert date2 in storage
    assert date3 in storage
    assert storage[date1][hour]['rainfall'] == rainfall1
    assert storage[date2][hour]['rainfall'] == rainfall2
    assert storage[date3][hour]['rainfall'] == rainfall3


def test_store_rainfall_same_hour_different_days():
    """Test that storing rainfall for the same hour on different days doesn't overwrite."""
    storage = {}
    date1 = '2024-01-15'
    date2 = '2024-01-16'
    hour = 10
    rainfall1 = 5.0
    rainfall2 = 12.5
    
    store_rainfall(date1, hour, rainfall1, storage)
    store_rainfall(date2, hour, rainfall2, storage)
    
    assert storage[date1][hour]['rainfall'] == rainfall1
    assert storage[date2][hour]['rainfall'] == rainfall2
    assert storage[date1][hour]['rainfall'] != storage[date2][hour]['rainfall']
