class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0  # private attribute

    def drive(self, km):
        if km > 0:
            self.__speed += km
            print(f"Driving at {self.__speed} km/h")
        else:
            print("\n[!] You can't drive backwards\n")

    def show_speed(self):
        return self.__speed


car = Car("Ford", "Focus")
car.drive(0)  # [!] You can't drive backwards
car.drive(150)  # Driving at 150 km/h
print(car.show_speed())  # 150
