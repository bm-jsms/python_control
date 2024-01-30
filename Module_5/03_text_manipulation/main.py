from modules.divider import divider as d


name = "Daniel"
age = 30

print("Hello my name is {} and I am {} years old".format(name, age))
print("Hello my name is {1} and I am {0} years old".format(age, name))
print(f"Hello my name is {name} and I am {age} years old")


d()


my_text = "\tHello World"
print(my_text)

print(my_text.strip())  # Removes leading and trailing whitespace
print(my_text.lstrip())  # Removes leading whitespace

print(my_text.upper())  # Converts to uppercase
print(my_text.lower())  # Converts to lowercase


d()


example = "a,b,c"
print(example.split(","))  # Splits string into a list


d()


s = "Hello World"
print(s.startswith("Hello"))  # Checks if string starts with "H"
print(s.endswith("World"))  # Checks if string ends with "d"
print(s.find("World"))  # Finds the index of the first occurrence of "W"
print(s.count("l"))  # Counts the number of occurrences of "l"
# print(s.index("Worlds"))  =>  Finds the index of the first occurrence of "W"


d()


l = ["Hello", "World"]
print(" ".join(l))  # Joins list elements with a space


d()


s = "hello world"
print(s.capitalize())  # Capitalizes first letter
print(s.title())  # Capitalizes first letter of each word
print(s.swapcase())  # Swaps case of each letter
