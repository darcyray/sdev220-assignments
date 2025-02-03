'''
Darcy Ralstin - Module 3 Lab
Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, \
such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and\
also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle \
type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the \
data in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
'''
class Vehicle():
    def __init__(self, type: str, year: int, make: str, model: str, num_doors: int, roof: str):
        self.type = type
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.roof = roof
    
class Car (Vehicle):
    pass
    
car_1 = Car('Car', 2022, "Toyota", "Corolla", 4, "sun roof")
print(car_1.type)
print(car_1.model)