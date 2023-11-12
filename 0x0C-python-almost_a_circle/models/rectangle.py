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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
