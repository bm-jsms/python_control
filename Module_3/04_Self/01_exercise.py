class Calculator:
    def __init__(self, num):
        self.num = num

    def add(self, ohter_num):
        return self.num + ohter_num

    def double_add(self, num1, num2):
        return self.add(num1) + self.add(num2)


cal = Calculator(2)
print(cal.add(2))  # 4
print(cal.double_add(2, 3))  # 9
