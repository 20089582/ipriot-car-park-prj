class Display:
    def __init__(self, id, car_park, message: str = "", is_on: bool = False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message}"
    
    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
    