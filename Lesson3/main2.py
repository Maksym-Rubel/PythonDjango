from abc import ABC, abstractmethod

class Ship(ABC): 
    def __init__(self,name):
        self.name = name


    @abstractmethod
    def display_info(self):
        pass

    def __str__(self):
        return f"Ship name ==> {self.name}"
    


class Frigate(Ship):
    def display_info(self):
        return f"Frigate name ==> {self.name}"
class Destroyer(Ship):
    def display_info(self):
        return f"Destroyer name ==> {self.name}"
class Cruiser(Ship):
    def display_info(self):
        return f"Cruiser name ==> {self.name}"
    

frigate = Frigate("TestFrig")
print(frigate.display_info())