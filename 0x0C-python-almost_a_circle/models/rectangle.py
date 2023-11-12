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
    """ Getter """
    def width(self):
        return (self.__width)

    @width.setter
    """ Setter """
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    """ getter """
    def height(self):
        return (self.__height)

    @height.setter
    """ setter """
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    """ getter """
    def x(self):
        return (self.__x)

    @x.setter
    """ setter """
    def x(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    """ getter """
    def y(self):
        return (self.__y)

    @y.setter
    """ setter """
    def y(self, value):
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
