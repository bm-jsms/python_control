from modules.divider import divider


class Person:
    def __init__(self, name, age):  # Person.__init__(matias, name, age)
        self.name = name
        self.age = age

    def say_hi(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old'


matias = Person('Matias', 25)

print(matias.name)  # Matias
print(matias.age)  # 25
print(matias.say_hi())  # Hello, my name is Matias and I am 25 years old


divider()


class Animal:
    def __init__(self, name, animal):  # Animal.__init__(bobby, name, animal)
        self.name = name
        self.animal = animal

    def description(self):
        return f'{self.name} is a {self.animal}'


dog = Animal('Bobby', 'dog')
cat = Animal('Dixy', 'cat')

print(dog.description())  # Bobby is a dog
