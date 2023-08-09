from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width must be positive")
        self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height must be positive")
        self.__height = height
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            raise ValueError("X must be positive")
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError("Y must be positive")
        self.__y = y