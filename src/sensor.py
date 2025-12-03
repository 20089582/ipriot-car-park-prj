from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, id, is_active: bool, car_park):
        """
        Initialize a Sensor instance.
        
        Args:
            id: Unique identifier for the sensor.
            is_active (bool): Whether the sensor is currently active.
            car_park: The CarPark instance this sensor monitors.
        """
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        """
        Return a string representation of the sensor.
        
        Returns:
            str: Sensor information including id and status.
        """
        status = "active" if self.is_active else "inactive"
        return f"Sensor id: {self.id}, Sensor status: {status}"
    
    @abstractmethod
    def update_car_park(self, plate):
        pass
    
    def _scan_plate(self):
        """
        Generate a fake license plate number.
        
        Returns:
            str: A fake plate number in the format 'FAKE-XXX'.
        """
        return 'FAKE-' + format(random.randint(0, 999), "03d")
    
    def detect_vehicle(self):
        """
        Detect a vehicle and update the car park.
        
        Generates a fake plate number and updates the car park based on
        the sensor type (entry or exit).
        """
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate: str):
        """
        Add a vehicle to the car park.
        
        Args:
            plate (str): The license plate number of the entering vehicle.
        """
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def update_car_park(self, plate: str):
        """
        Remove a vehicle from the car park.
        
        Args:
            plate (str): The license plate number of the exiting vehicle.
        """
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
    
    def _scan_plate(self):
        """
        Select a random plate from cars currently in the car park.
        
        This is a workaround for simulating exit sensor behavior.
        
        Returns:
            str: A randomly selected plate from the car park.
        """
        return random.choice(self.car_park.plates)