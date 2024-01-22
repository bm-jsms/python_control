my_set = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5}

print(my_set)  # {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>
# print(my_set[0])  =>  TypeError: 'set' object is not subscriptable

my_set.add(7)
my_set.add(0)

print(my_set)  # {0, 1, 2, 3, 4, 5, 7}

my_set.update([8, 9, 10])

print(my_set)  # {0, 1, 2, 3, 4, 5, 7, 8, 9, 10}

my_set.remove(10)

print(my_set)  # {0, 1, 2, 3, 4, 5, 7, 8, 9}

# my_set.remove(10)  =>  KeyError: 10
my_set.discard(10)  # No error
my_set.discard(9)

print(my_set)  # {0, 1, 2, 3, 4, 5, 7, 8}
