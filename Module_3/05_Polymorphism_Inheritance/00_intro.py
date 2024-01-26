from modules.divider import divider


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


dog = Dog("Max")
cat = Cat("Misty")
cat_2 = Animal("Misty")

dog.speak()  # Woof!
cat.speak()  # Meow!
# cat_2.speak()  =>  NotImplementedError: Subclass must implement abstract method


divider()


def do_speak(obj):
    print(f"{obj.name} says: {obj.speak()}")


do_speak(dog)  # Max says: Woof!
