class Square:
    def __init__(self, size):
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size

