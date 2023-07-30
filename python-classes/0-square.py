class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def perimeter(self):
        return 4 * self.__size

    def __str__(self):
        return f"Square with side length {self.__size}"

# Example usage:
if __name__ == "__main__":
    square1 = Square(5)
    print(square1)  # Output: Square with side length 5
    print("Area:", square1.area())  # Output: Area: 25
    print("Perimeter:", square1.perimeter())  # Output: Perimeter: 20

    square2 = Square(10)
    print(square2)  # Output: Square with side length 10
    print("Area:", square2.area())  # Output: Area: 100
    print("Perimeter:", square2.perimeter())  # Output: Perimeter: 40
