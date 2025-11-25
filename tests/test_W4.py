'''algorithm for storing the hourly values of temperature (max, min, average), rainfall
and wind speed (min and max) in a table. The temperature values are stored in the
control center, the other two values come hourly from the respective sensors'''

from src.tdd_practice.weather_storage import store_temperature

'''Test case 1 Store temperature data
3 parameters for temperature: max, min, average
for 1 hour we receive 3 values for temperature: max, min, average
for the storage for now we just use dictionary to store the data
'''
def test_store_temperature_data():
    temperature_data = {
        'max': 10,
        'min': 5,
        'average': 7.5
    }

    hour = 10
    storage = {}
    
    store_temperature(hour, temperature_data, storage)
    
    # ASSERT: Verify the data was stored correctly
    assert hour in storage
    assert storage[hour]['temperature'] == {
        'max': 10,
        'min': 5,
        'average': 7.5
    }
    