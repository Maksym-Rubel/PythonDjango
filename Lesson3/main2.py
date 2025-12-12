# from abc import ABC, abstractmethod

# class Ship(ABC): 
#     def __init__(self,name):
#         self.name = name


#     @abstractmethod
#     def display_info(self):
#         pass

#     def __str__(self):
#         return f"Ship name ==> {self.name}"
    


# class Frigate(Ship):
#     def display_info(self):
#         return f"Frigate name ==> {self.name}"
# class Destroyer(Ship):
#     def display_info(self):
#         return f"Destroyer name ==> {self.name}"
# class Cruiser(Ship):
#     def display_info(self):
#         return f"Cruiser name ==> {self.name}"
    

# frigate = Frigate("TestFrig")
# print(frigate.display_info())



class AirPlane:
    def __init__(self,model,capacity):
        self.model = model
        self.capacity = capacity

    def __str__(self):
        return f"AirPlane model ==> {self.model}, capacity ==> {self.capacity}"
    
    def __int__(self):
        return self.capacity

    def __eq__(self,other):
        if(self.model == other.model):
            return True
        return False
    
    def __add__(self,value):
        return self.capacity + value
    def __sub__(self,value):
        return self.capacity - value
    
    def __gt__(self, other):
        return self.capacity > other.capacity

        


plane1 = AirPlane("Boeing 747", 660)
plane2 = AirPlane("Boeing 747", 416)
plane3 = AirPlane("Airbus A380", 853)
print(plane1 == plane2)  # True

print(plane1 + 100)  # 760
print(plane3 - 100)  # 760

print("plane1 > plane2: ", plane1 > plane2)
print("plane3 < plane2: ", plane3 < plane2)


print(plane1)
print(int(plane1))

