class Square:
    """
    This class defines a square with a size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must b
        """
        Calculates the area of the squa:
            int: The area of the square.
        """
        return self.__size ** 2

