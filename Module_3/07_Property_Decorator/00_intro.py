def my_decorator(function):  # higher order function
    def inner():
        print("\nBefore function")
        function()
        print("After function\n")
    return inner


@my_decorator  # decorator
def greet():
    print("Hello World")


greet()  # calling function


# @property  =>  getters and setters
