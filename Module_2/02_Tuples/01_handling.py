from modules.divider import divider


my_first_tuple = (1, 2, 3)
my_second_tuple = (4, 5, 6)

# my_tuple = my_first_tuple * 2
# print(my_tuple)  # (1, 2, 3, 1, 2, 3)

my_tuple = my_first_tuple + my_second_tuple
print(my_tuple)  # (1, 2, 3, 4, 5, 6


divider()


number_pairs = tuple(i for i in range(1, 11) if i % 2 == 0)
print(number_pairs)  # (2, 4, 6, 8, 10)


divider()


db1_credential = ("JSMS", "123456")
db2_credential = ("Hackerman", "hackerman123")

try:
    db1_credential[0] = "John"
except TypeError:
    print("Cannot change elements in a tuple")