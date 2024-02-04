from modules.divider import divider as d
import re


d()


def validate_email(email):
    # This is a regular expression
    pattern = "[A-Za-z0-9._+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}"
    if re.findall(pattern, email):
        return True
    else:
        return False


print(validate_email("admin69@admin.io"))  # True
print(validate_email("xxxxxxx@xxxxx"))  # False
print(validate_email("email@io"))  # False
print(validate_email("email@email.com"))  # True


d()


text = "car, cart, carrot, carpet, scar"
"""
This isnt what we want => ['car', 'car', 'car', 'car', 'car']
"""
# print(re.findall("car", text)) => ['car', 'car', 'car', 'car', 'car']
# print(re.findall(r"\bcar", text))  => ['car', 'car', 'car', 'car']
print(re.findall(r"\bcar\b", text))  # ['car']
