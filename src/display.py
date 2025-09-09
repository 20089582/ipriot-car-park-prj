
class Display:
    def __init__(self,id:int,message:str="",is_on:bool=False):
        '''intialises variables'''
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        '''spits out information about the display'''
        return f"Display {self.id}: {self.message}"
    
    def update(self, data:dict):
        '''updates the display values'''
        for key, value in data.items():
            print(f"{key}: {value}")
    