'''
Darcy Ralstin - Module 3 Lab
Description: 
Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, \
such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and \
also contain the following attributes:year, make, model, doors (2 or 4), roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle \
type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the \
data in the attributes above.
The app will then output the data in an easy-to-read and understandable format.
'''
class Vehicle():
    def __init__(self, type: str):
      self.type = type
    
class Automobile (Vehicle):
    def __init__(self, type: str, year: int, make: str, model: str, num_doors: int, roof: str):
      super().__init__(type)
      self.year = year
      self.make = make
      self.model = model
      self.num_doors = num_doors
      self.roof = roof
      
def main():
  vehicle_type = "car"
  year = int(input("Enter the year of the car: "))
  make = input("Enter the make of the car: ")
  model = input("Enter the model of the car: ")
  num_doors = int(input("Enter the number of doors (2 or 4): "))
  roof = input("Enter roof type (solid or sun roof): ")
  
  car = Automobile(vehicle_type, year, make, model, num_doors, roof)
    
  print(f"Vehicle type: {car.type}")
  print(f"Year: {car.year}")
  print(f"Make: {car.make}")
  print(f"Model: {car.model}")
  print(f"Number of doors: {car.num_doors}")
  print(f"Type of roof: {car.roof}")

  main()
