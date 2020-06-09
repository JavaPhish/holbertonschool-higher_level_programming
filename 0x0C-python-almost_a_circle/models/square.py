#!/usr/bin/python3
""" square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square based off of Rectangle (And hopefully doesnt circular import)"""

    def __init__(self, size, x=0, y=0, id=None):
        """ inherets all attributes from rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str rep """
        str_size = self.get_width()
        str_id = "({})".format(self.id)
        x_and_y = "{}/{}".format(self.get_x(), self.get_y())
        return ("[Square] {} {} - {}".format(str_id, x_and_y, str_size))

    def to_dictionary(self):
        """ dictionary representation of the square (Override of rect)"""
        dic_repr = {}
        dic_repr["id"] = self.id
        dic_repr["x"] = self.get_x()
        dic_repr["size"] = self.get_size()
        dic_repr["y"] = self.get_y()

        return dic_repr

    def update(self, *args, **kwargs):
        """ updates the current instance with given values """
        if len(args) > 0:
            if (len(args) > 0):
                self.id = args[0]
            if (len(args) > 1):
                self.set_width(args[1])
                self.set_height(args[1])
            if (len(args) > 2):
                self.set_x(args[2])
            if (len(args) > 3):
                self.set_y(args[3])
        else:
            for key in kwargs:
                if key is "size":
                    self.set_size(kwargs[key])
                if key is "x":
                    self.set_x(kwargs[key])
                if key is "y":
                    self.set_y(kwargs[key])
                if key is "id":
                    self.id = kwargs[key]

    def set_size(self, size):
        """ sets size, assigns rectangle width and height """
        self.set_width(size)
        self.set_height(size)

    def get_size(self):
        """ gets the size, or the width of the square (height = width) """
        return self.get_width()

    size = property(get_size, set_size)
