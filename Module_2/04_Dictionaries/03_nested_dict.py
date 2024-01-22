from modules.divider import divider


my_dict = {
    "name": "Thomas",
    "hobbies": {
        "sport": "football",
        "music": "guitar",
    },
    "age": 20,
}

print(my_dict["hobbies"]["sport"])  # football
print(my_dict["hobbies"]["music"])  # guitar


divider()


my_dict = {
    "name": "Thomas",
    "age": 20,
    "country": "Germany",
}

for element in my_dict:
    print(element)

divider()

for element in my_dict.values():
    print(element)

divider()

for element in my_dict.items():
    print(element)

divider()

for key, value in my_dict.items():
    print(f"{key}: {value}")
