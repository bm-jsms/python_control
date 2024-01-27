class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __str__(self):
        return f"{self.x}, {self.y}"


p1 = Point(2, 8)
p2 = Point(4, 9)

print(p1 + p2)  # 6, 17
