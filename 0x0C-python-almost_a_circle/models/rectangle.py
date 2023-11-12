from models.base import Base
""" Imported module """


class Rectangle(Base):
    """ Class definition """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor:
        Args:
            width: the first input
            height: the second input
            x: the third input
            y: the forth input
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area method:
        Return:
            the result
        """
        return (self.__width * self.__height)

    def display(self):
        """ display rectangle method """
        for i in range(self.height):
            for j in range(self.width):
                if (j == self.width - 1):
                    print("#")
                else:
                    print("#", end='')
