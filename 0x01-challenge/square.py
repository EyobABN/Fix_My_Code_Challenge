#!/usr/bin/python3
""" A module for a square representation. """


class Square:
    """Represents a rectangle with equal sides."""
    side = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new square. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Computes the area of the square. """
        return self.side ^ 2

    def perimeter_of_my_square(self):
        """ Computes the perimeter of the square. """
        return self.side * 4

    def __str__(self):
        """ Computes the string format of this square. """
        return "{}/{}".format(self.side, self.side)


if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
