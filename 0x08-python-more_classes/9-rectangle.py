#!/usr/bin/python3
""" AAAAAAHHHHH """


class Rectangle:
    """ Rectangle: a class. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init for rectangle """
        Rectangle.number_of_instances += 1
        self.set_height(height)
        self.set_width(width)

    @classmethod
    def square(cls, size=0):
        """ Returns a square insance (width == height == size) """
        return cls(size, size)

    def bigger_or_equal(rect_1, rect_2):
        """ Compares two rectangles size, even tho size doesnt matter """
        if (type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return (rect_2)
        return (rect_1)

    def __del__(self):
        """ DESTRUCTION OF THE INSTANCE MUAHAHAHA """
        Rectangle.number_of_instances -= 1
        del self
        print("Bye rectangle...")

    def __repr__(self):
        """ Object REPResentation of a rectangle """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __str__(self):
        """ str representation of a rect """
        if (self.__width is 0):
            return ("")
        if (self.__height is 0):
            return ("")
        n_str = self.__height * ((self.width * str(self.print_symbol)) + "\n")
        return (n_str[0:-1])

    def area(self):
        """ Returns the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ The perimeter of the rectangle """
        if (self.__width is 0):
            return (0)
        if (self.__height is 0):
            return (0)
        return (2 * (self.__height + self.__width))

    # setter
    def set_width(self, n_width):
        """ Setter for the width """
        if type(n_width) is not int:
            raise TypeError("width must be an integer")
        if n_width < 0:
            raise ValueError("width must be >= 0")

        self.__width = n_width

    # getter
    def get_width(self):
        """ Getter for private inst width """
        return self.__width

    width = property(get_width, set_width)

    # setter
    def set_height(self, n_height):
        """ Setter for private inst height """
        if type(n_height) is not int:
            raise TypeError("height must be an integer")
        if n_height < 0:
            raise ValueError("height must be >= 0")

        self.__height = n_height

    # getter
    def get_height(self):
        """ Getter for private inst height """
        return self.__height

    height = property(get_height, set_height)
