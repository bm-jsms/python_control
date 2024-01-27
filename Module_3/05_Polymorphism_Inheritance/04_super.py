class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def introduce(self):
        return f"{super().introduce()} I earn {self.salary} per month."


person = Employee("John", 36, 2500)
print(person.introduce())
