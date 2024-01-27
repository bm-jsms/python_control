from modules.divider import divider


class Box:

    def __init__(self, *fruits):  # *fruits is a tuple
        self.fruits = fruits

    def show_fruits(self):
        # print(type(self.fruits))
        print("Fruits in the box:")
        for fruit in self.fruits:
            print(f"- {fruit}")

    def __len__(self):
        return len(self.fruits)


box = Box("apple", "banana", "orange", "pear")
box.show_fruits()
print(len(box))


divider()


class Pizza:

    def __init__(self, size, *toppings):
        self.size = size
        self.toppings = toppings

    def description(self):
        print(f"This is a {self.size} inch pizza with the following toppings: {' - '.join(self.toppings)}")


pizza = Pizza(12, "cheese", "tomato", "ham", "mushrooms")
pizza.description()


divider()


class Mylist:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, index):
        return self.data[index]


list_1 = Mylist()
print(list_1[2])


divider()


class Greet:
    def __init__(self, greet):
        self.greet = greet

    def __call__(self, name):
        return f"{self.greet} {name}"


hello = Greet("Hello")
print(hello("Lucas"))
print(hello("Diana"))