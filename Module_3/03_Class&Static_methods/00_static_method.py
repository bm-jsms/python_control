class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def rest(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else "You can't divide by zero"


print(Calculator.add(69, 45))
print(Calculator.rest(25, 3))
print(Calculator.multiply(12, 3))
print(Calculator.divide(21, 3))
print(Calculator.divide(6, 0))
