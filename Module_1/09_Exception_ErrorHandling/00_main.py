from modules.divider import divider

try:

    num = input("Enter a number: ")
    num_two = input("Enter another number: ")
    result = int(num) / int(num_two)

except ZeroDivisionError:

    print("\nDivided by zero")

except TypeError:

    print("\nType error")

else:

    print(f"\n {num} / {num_two} = {result}")

finally:

    print("\nThis is going to be executed no matter what")


divider()


x = -4

if x < 0:
    raise Exception("x should be positive")
