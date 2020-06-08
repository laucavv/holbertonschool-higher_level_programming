#!/usr/bin/python3
"""Class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Builder

        Args:
            size (int): square size
            x (int, optional):x-axis position Defaults to 0.
            y (int, optional): y-axis position. Defaults to 0.
            id (int, optional):object id  Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            method so that it returns
            [Square] (<id>) <x>/<y> - <size>
        """

        out = "[Square] ({}) {}/{} - ".format(self.id, self.x, self.y)
        out += "{}".format(self.width)
        return out

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ That assigns a key/value argument to attributes: """
        atribute = ["id", "size", "x", "y"]
        if args:
            for count, item in enumerate(args):
                if count < 4:
                    setattr(self, atribute[count], item)
        else:
            for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """That returns the dictionary representation of a square """
        atribute = ["id", "size", "x", "y"]
        dir = {}
        for key in atribute:
            dir[key] = getattr(self, key)
        return dir
