import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_entry_sensor_detects_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 99)

    def test_exit_sensor_detects_vehicle(self):
        # Add a car first so there is something to remove
        self.car_park.add_car("FAKE-001")
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 100)
