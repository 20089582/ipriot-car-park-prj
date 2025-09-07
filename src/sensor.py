class Sensor:
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "active" if self.is_active else "inactive"
        return f"Sensor id: {self.id}, Sensor status: {status}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass