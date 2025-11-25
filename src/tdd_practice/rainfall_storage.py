def store_rainfall(hour: int, rainfall_value: float, storage: dict) -> None:
    if hour not in storage:
        storage[hour] = {}
    storage[hour]['rainfall'] = rainfall_value