from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location: str, capacity: int, plates: list = None, sensors: list[Sensor] = None , displays: list[Display] = None):
        """initialises variables"""
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        
    def __str__(self):
        """spits out information about the car park"""
        return f"Location: {self.location}, Bay capacity: {self.capacity}"
    
    def register(self, component):
        """registers a sensor or display component"""
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        """adds car and updates display"""
        self.plates.append(plate)
        self.update_displays()
    def remove_car(self, plate):
        """removes car and updates display"""
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            raise ValueError(f"Plate: {plate} not found")
    @property
    def available_bays(self):
        """calculates available bays"""
        return max(0, self.capacity - len(self.plates))
    
    def update_displays(self):
        """sends current data to the display"""
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)