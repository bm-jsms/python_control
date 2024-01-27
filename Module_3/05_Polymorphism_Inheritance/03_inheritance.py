class A:

    def __init__(self, x):
        self.x = x
        print(f" X = {self.x}")


class B(A):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        print(f" Y = {self.y}")


b = B(10, 20)
