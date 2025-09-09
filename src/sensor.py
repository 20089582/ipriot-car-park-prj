from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        '''intialises variables'''
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        '''spits out information about the sensor'''
        status = "active" if self.is_active else "inactive"
        return f"Sensor id: {self.id}, Sensor status: {status}"
    
    @abstractmethod
    def update_car_park(self, plate):
        pass
    
    def _scan_plate(self):
        '''creates a fake plate number'''
        return 'FAKE-' + format(random.randint(0, 999), "03d")
    
    def detect_vehicle(self):
        '''creates a fake plate then updates car park based on the sensor used to gather the information'''
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        '''adds the plate number to the car park'''
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        '''removes a plate number from the car park'''        
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
    
    def _scan_plate(self):
        '''a work around for cars exiting the car park'''
        return random.choice(self.car_park.plates)