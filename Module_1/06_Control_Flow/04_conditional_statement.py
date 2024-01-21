from modules.divider import divider


number = 23
if number < 0:
    print("The number is negative")
elif number == 0:
    print("The number is zero")
else:
    print("The number is positive")


divider()


i = 0

while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
else:
    print("Loop is over")

print("The end")
