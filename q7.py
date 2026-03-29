class Car:
    """
    Task 1:
    A class representing a car with make, model, and year attributes.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Task 2: Create an instance and call the method
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()  # Output: 2020 Toyota Corolla
