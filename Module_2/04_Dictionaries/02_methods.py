my_dictionary = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

my_dictionary2 = {
    "profession": "Developer",
}


print(my_dictionary.get("age", "Not found"))  # 36
print(my_dictionary.get("ag", "Not found"))  # Not found

my_dictionary.update(my_dictionary2)

print(my_dictionary)
