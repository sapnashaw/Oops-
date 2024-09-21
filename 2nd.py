#2. Write a Python class for a `Car` with attributes for `make`, `model`, and `year`. Include a method to display
#   the car's information.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")


my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
