#!/usr/bin/python3
""" contains rect """


from models.base import Base


class Rectangle(Base):
    """ based off base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        sup_b = Base(id)
        self.id = sup_b.id

    def __str__(self):
        """ string representation of the rect """
        str_id = "({})".format(self.id)
        x_and_y = "{}/{}".format(self.__x, self.__y)
        w_and_h = "{}/{}".format(self.__width, self.__height)
        return ("[Rectangle] {} {} - {}".format(str_id, x_and_y, w_and_h))

    def to_dictionary(self):
        """ dictionary representation of the rectangle """
        dic_repr = {}
        dic_repr["x"] = self.__x
        dic_repr["y"] = self.__y
        dic_repr["id"] = self.id
        dic_repr["height"] = self.__height
        dic_repr["width"] = self.__width

        return dic_repr

    def update(self, *args, **kwargs):
        """ updates the current instance with given values """
        if len(args) > 0:
            if (len(args) > 0):
                self.id = args[0]
            if (len(args) > 1):
                self.set_width(args[1])
            if (len(args) > 2):
                self.set_height(args[2])
            if (len(args) > 3):
                self.set_x(args[3])
            if (len(args) > 4):
                self.set_y(args[4])
        else:
            for key in kwargs:
                if key is "height":
                    self.set_height(kwargs[key])
                if key is "width":
                    self.set_width(kwargs[key])
                if key is "x":
                    self.set_x(kwargs[key])
                if key is "y":
                    self.set_y(kwargs[key])
                if key is "id":
                    self.id = kwargs[key]

    def display(self):
        """ prints the rectangle in stdout """
        w_str = ((self.__x * " ") + (self.__width * "#") + "\n")

        if (self.__y > 0):
            print("\n" * (self.__y - 1))
        print(self.__height * w_str, end="")

    def area(self):
        """ returns the are of the rectangle """
        return (self.__height * self.__width)

    def set_x(self, x):
        """ setter for x """
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    def get_x(self):
        """ get x """
        return self.__x

    x = property(get_x, set_x)

    def set_y(self, y):
        """ setter for y """
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def get_y(self):
        """ get y """
        return self.__y

    y = property(get_y, set_y)

    def set_width(self, width):
        """ Setter for width """
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width < 1):
            raise ValueError("width must be > 0")
        self.__width = width

    def get_width(self):
        """ Getter for width """
        return self.__width

    width = property(get_width, set_width)

    def set_height(self, height):
        """ Setter for height """
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height < 1):
            raise ValueError("height must be > 0")
        self.__height = height

    def get_height(self):
        """ Getter for height """
        return self.__height

    height = property(get_height, set_height)
