class Display:
    def __init__(self, id, car_park, message: str = "", is_on: bool = False):
        '''intialises variables'''
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        '''spits out information about the display'''
        return f"Display {self.id}: {self.message}"
    
    def update(self, data):
        '''updates the display values'''
        for key, value in data.items():
            print(f"{key}: {value}")
    