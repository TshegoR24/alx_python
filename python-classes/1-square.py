class Square:
    def __init__(self, size=0):
        self.__size = 0  # Initialize size to 0 by default
        self.size = size  # Call the property setter to handle validations

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
