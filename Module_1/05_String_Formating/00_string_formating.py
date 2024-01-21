name = "JSMS"
rol = "lammer"
age = 19


# Method 1
print("Hello I am %s and I am a %s. I am currently %d years old." % (name, rol, age))

# Method 2
print("Hello I am {} and I am a {}. I am currently {} years old.".format(name, rol, age))

# Method 3
print("Hello I am {0} and I am a {1}. I am currently {2} years old.".format(name, rol, age))

# Method 4
print("Hello I am {name} and I am a {rol}. I am currently {age} years old.".format(name=name, rol=rol, age=age))

# Method 5 (recommended)
print(f"Hello I am {name} and I am a {rol}. I am currently {age} years old.")
