from modules.divider import divider 


my_dictionary = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

print(type(my_dictionary))  # <class 'dict'>
print(my_dictionary)  # {'name': 'John', 'age': 36, 'country': 'Norway'}
print(my_dictionary["age"])  # 36

my_dictionary["age"] = 40
print(my_dictionary)  # {'name': 'John', 'age': 40, 'country': 'Norway'}

my_dictionary["city"] = "Barcelona"
print(my_dictionary)  # {'name': 'John', 'age': 40, 'country': 'Norway', 'city': 'Barcelona'}

del my_dictionary["age"]
print(my_dictionary)  # {'name': 'John', 'country': 'Norway', 'city': 'Barcelona'}


divider()


if "city" in my_dictionary:
    print("Yes, 'city' is one of the keys in the dictionary")
else:
    print("No, 'city' is not one of the keys in the dictionary")


divider()


for key, value in my_dictionary.items():
    print(f"{key}: {value}")


divider()


print(f"Length of the dictionary: {len(my_dictionary)}")


divider()


my_dictionary.clear()
print(my_dictionary)  # {}