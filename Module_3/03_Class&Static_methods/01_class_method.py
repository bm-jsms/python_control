class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def sport_car(cls, brand):
        return cls(brand, "Sport")

    def __str__(self):
        return f"\n[!] The car {self.brand} is a {self.model} car"


car_1 = print(Car.sport_car("Ferrari"))
car_2 = print(Car.sport_car("Lamborghini"))