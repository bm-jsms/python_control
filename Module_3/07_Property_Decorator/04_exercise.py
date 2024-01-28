class Circumference:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.__radius = radius


c = Circumference(10)
print(c.radius)  # 10
print(c.diameter)  # 20
print(c.area)  # 314.0

c.radius = 20
print(c.radius)  # 20
print(c.diameter)  # 40
print(c.area)  # 1256.0
