#!/usr/bin/python3
"""
Module containing the Base class.
"""

class Base:
    """
    The Base class for managing id attributes in other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The id of the instance. If None, will use the next value of __nb_objects.

        Attributes:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
