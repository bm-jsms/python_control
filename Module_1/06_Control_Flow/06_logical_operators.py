from modules.divider import divider

age = 20
nationality = "Canadian"

if age >= 18 and nationality == "Canadian":
    print("You are eligible to vote in Canada")

elif age >= 18 or nationality == "Canadian":
    print("You are eligible to vote in Canada")

else:
    print("You are not eligible to vote in Canada")


divider()


my_list = [1, 2, 3, 4, 5]

if 6 or 3 in my_list:
    print("Yes")
else:
    print("No")


divider()

my_value = True

if not my_value:
    print("The value is false")
else:
    print("The value is true")
