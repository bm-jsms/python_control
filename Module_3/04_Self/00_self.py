from modules.divider import divider


class Person:
    def __init__(self, name, age):  # Person.__init__(marcelo,name,age)
        self.name = name  # marcelo.name = name
        self.age = age  # marcelo.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}")  # marcelo.name


marcelo = Person("Marcelo", 20)

print(marcelo.name)  # Marcelo
print(marcelo.age)  # 20
print(marcelo.say_hello())  # Hello, my name is Marcelo


divider()


class Test:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

    def say_hello(obj):
        print(f"Hello, my name is {obj.name}")


test = Test("Marcelo", 20)

print(test.name)  # Marcelo
print(test.age)  # 20
print(test.say_hello())  # Hello, my name is Marcelo
