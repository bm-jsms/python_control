from modules.divider import divider


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    (property)
    def area(self):
        return f"\n[+] Area: {self.width * self.height}"

    def __str__(self) -> str:
        return f"\nRectangle: [width: {self.width}, height: {self.height}]"

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


rect = Rectangle(10, 20)
print(rect)
print(rect.area())  # 200


divider()


rect1 = Rectangle(5, 10)
# rect2 = Rectangle(7, 3)
rect2 = Rectangle(5, 10)

print(f"Are rect1 and rect2 equal?: {rect1 == rect2}")
