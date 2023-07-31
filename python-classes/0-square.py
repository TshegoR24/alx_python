class Square:
    def __init__(self, size):
        self.__size = size

    def __str__(self):
        return f"<class '{type(self).__module__}.{type(self).__name__}'>"

    def __repr__(self):
        return f"{{'_Square__size': {self.__size}}}"

    def __getattr__(self, item):
        if item == 'size':
            raise AttributeError("'Square' object has no attribute 'size'")
        elif item == '__size':
            raise AttributeError("'Square' object has no attribute '__size'")
        else:
            raise AttributeError(f"'Square' object has no attribute '{item}'")


# Test
square_instance = Square(3)
print(square_instance)
print(square_instance.__dict__)
print(square_instance.size)
print(square_instance.__size)

