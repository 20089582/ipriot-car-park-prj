class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Location: {self.location}, bay capacity: {self.capacity}"