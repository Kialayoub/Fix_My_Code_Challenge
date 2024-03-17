#!/usr/bin/python3
""" square class"""
class Square():
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ square object """
    square = Square(width=12, height=9)
    print(square)
    print(square.area_of_my_square())
    print(square.permiter_of_my_square())
