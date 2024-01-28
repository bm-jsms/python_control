from modules.divider import divider as d


# *args
def sum(*args):
    print(type(args))
    s = 0
    for i in args:
        s += i
    return s


print(sum(2, 8, 6, 12, 8))


d()


# **kwargs
def introduce(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")


introduce(name="John", age=30, country="USA")
