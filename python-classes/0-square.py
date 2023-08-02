class Square:
    """
    This class defines a square by its size.
    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size):
        """
        This method initializes the size of the square.
        Args:
            size (int): The size of the square.
        """
        self.size = size
    def area(self):
        """
        This method calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.size ** 2
    def perimeter(self):
        """
        This method calculates the perimeter of the square.
        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.size

