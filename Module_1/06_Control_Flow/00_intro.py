from modules.divider import divider

for i in range(5):
    print(i)


divider()


names = ["JSMS", "Jhon", "Jane", "Jason"]
for i, name in enumerate(names):
    print(f"{i + 1}: {name}")


divider()


i = 0
while i < 5:
    print(i)
    i += 1


divider()


fruits = {"Apple": 10, "Banana": 20, "Orange": 30}

for fruit, count in fruits.items():
    print(f"There are {count} {fruit}s")
