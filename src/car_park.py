from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
    def __str__(self):
        return f"Location: {self.location}, bay capacity: {self.capacity}"
    
    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.sensors.append(component)
    
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
    
    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))
    
    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)