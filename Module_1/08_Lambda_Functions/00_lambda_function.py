from modules.divider import divider


greet = lambda: print("Hello World")
greet() # Hello World


divider()


square = lambda x: x**2
print(square(5)) # 25
print(square(7)) # 49


divider()


sum = lambda x, y: x + y
print(sum(5, 7)) # 12
print(sum(10, 20)) # 30


divider()


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
