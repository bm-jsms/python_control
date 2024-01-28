class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        print("getter")
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            print("setter")
            self._age = value
        else:
            raise ValueError("Invalid value")


daniel = Person("Daniel", 23)
# daniel.age = -1  =>  Error
daniel.age = 24  # setter
print(daniel.age)  # getter
