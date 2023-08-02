class Square:
    """
    This class represents a square with a private instance attribute 'size'.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with the given size.

        Parameters:
        size (int): The size of the square (side length).
        """
        self._size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self._size * self._size

    def perimeter(self):
        """
        Calculate and return the perimeter of the square.

        Returns:
        int: The perimeter of the square.
        """
        return 4 * self._size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: A string representation of the square.
        """
        return f"Square with side length {self._size}"


