class Example:
    def __init__(self):
        # protected attribute
        self._protected = "Im protected"

        # private attribute
        self.__private = "Im private"


example = Example()


# Protected
"""You shouldn't call protected attributes directly (but you can).
Only the class and its subclasses can access protected attributes.
"""
# print(example._protected)  =>  Im protected


# Private
"""You can't call private attributes directly."""
# print(example.__private)  =>  AttributeError: 'Example' object has no attribute '__private'
