class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        return f"Vehicle: {self.brand} {self.model}"


class Car(Vehicle):

    def description(self):
        return f"Car: {self.brand} {self.model}"


class Motorcycle(Vehicle):

    def description(self):
        return f"Motorcycle: {self.brand} {self.model}"


def describe_vehicle(vehicle):  # Polymorphism
    print(vehicle.description())


car = Car("Ford", "Mustang")
describe_vehicle(car)  # Car: Ford Mustang

motorcycle = Motorcycle("Honda", "CBR")
describe_vehicle(motorcycle)  # Motorcycle: Honda CBR
