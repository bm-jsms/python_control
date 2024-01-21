from modules.divider import divider

# def => define
# def function_name():
# return => return the value


def greeting(name):
    print(f"Hello {name}")


greeting("John")  # Hello John
greeting("Jane")  # Hello Jane


divider()


def add(a, b):
    return a + b


print(f"[+] The sum of 8 and 6 is {add(8, 6)}")
