from modules.divider import divider


example = (1, 2, 3, 4, 5)
print(example)  # (1, 2, 3, 4, 5)
print(type(example))  # <class 'tuple'>

print(example[0])  # 1
print(example[1:4])  # (2, 3, 4)

# example[0] = 10   => TypeError: 'tuple' object does not support item assignment


divider()


my_tuple = (1, "Hello", [1, 2, 3], {"name": "John"})
print(my_tuple)  # (1, 'Hello', [1, 2, 3], {'name': 'John'})


divider()


my_tuple = (1, 2, 3, 4)

print(my_tuple)  # (1, 2, 3, 4)

a, b, c, d = my_tuple

print(a)  # 1
print(b)  # 2
print(c)  # 3
print(d)  # 4
