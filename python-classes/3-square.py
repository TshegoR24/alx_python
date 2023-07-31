class Square:
    # Private instance attribute: size
    def __init__(self, size=0):
        self._size = size
    # Property def size(self): to retrieve it
    @property
    def size(self):
        return self._size
    # Property setter def size(self, value): to set it:
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
    # Instantiation with optional size: def __init__(self, size=0):
    # Public instance method: def area(self): that returns the current square area
    def area(self):
        return self._size * self._size
