
class Display:
    def __init__(self,id:int,message:str="",is_on:bool=False):
        """initialises variables"""
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        """spits out information about the display"""
        return f"Display {self.id}: {self.message}"
    
    def update(self, data:dict):
        """updates the display values"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            print(f"{key}: {value}")
    