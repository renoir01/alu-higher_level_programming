#!/usr/bin/python3
<<<<<<< HEAD
'''Defines a class square that inherits from the Rectangle class
'''
=======
"""
the class Square that inherits from Rectangle

In the path models/square.py

Class Square inherits from Rectangle

As you know, a Square is a special Rectangle,

so it makes sense this class Square inherits from Rectangle.

Now you have a Square class who has the same attributes and same methods.
"""


>>>>>>> 191e4a2018aa5ae4d7c78cb564c710d0c03342f9
from models.rectangle import Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    '''Defines a class Square that inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes new square object

        Args:
           size (int): The size of the square to be initialized
           x (int): The horizontal position of the square
           y (int): The vaertical position of the square
           id (int): Instance id
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return string representation of a square object
        '''
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        '''Getter for the size of square instance
        '''
        return self.width

    @size.setter
    def size(self, size):
        '''Setter for size of square object

        Args:
           size (int): The size to be set for square object
        '''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''Updates the instance attribute values with the values specified

        Args:
           args (list):
              1st argument should be the id attribute
              2nd argument should be the size attribute
              3rd argument should be the x attribute
              4th argument should be the y attribute
           kwargs (dict):
              Contains keyword argument to be updated
        '''
        if len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, attr in enumerate(args):
                setattr(self, attributes[i], attr)
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle object
        '''
        def remove_prefix(value):
            '''Converts private attribute format to normal attribute name

            Args:
               value (str): The value to be converted
            '''
            if value[:12] == "_Rectangle__":
                if value[12:] in ["width", "height"]:
                    return "size"
                else:
                    return value[12:]
            return value

        return {remove_prefix(key): self.__dict__[key] for key in
                self.__dict__.keys()}
=======
    """
    Class Square inherits from Rectangle

    Class constructor: def __init__(self, size, x=0, y=0, id=None)

    You must not create new attributes for this class,

    use all attributes of Rectangle -

    As reminder: a Square is a Rectangle with the same width and height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height

        his super call will use the logic of the __init__ of the

        Rectangle class. The width and height must be assigned

        to the value of size.

        All width, height, x and y validation must inherit from Rectangle -

        same behavior in case of wrong data
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The overloading __str__ method should return

        [Square] (<id>) <x>/<y> - <size> -

        in our case, width or height
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """The class Square by adding the public getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        the class Square by adding the public setter size

        The setter should assign (in this order) the width

        and the height - with the same value

        The setter should have the same value validation

        as the Rectangle for width and height -

        No need to change the exception error

        message (It should be the one from width)
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        the class Square by adding the public method

        def update(self, *args, **kwargs)

        that assigns attributes:

        *args is the list of arguments - no-keyworded arguments

        1st argument should be the id attribute

        2nd argument should be the size attribute

        3rd argument should be the x attribute

        4th argument should be the y attribute

        **kwargs can be thought of as a double pointer to a dictionary

        key/value (keyworded arguments)

        **kwargs must be skipped if *args exists and is not empty

        Each key in this dictionary represents an attribute to the instance
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                    self.height = args[1]
                elif i == 2:
                    self.x = args[2]
                else:
                    self.y = args[3]
        else:
            copy_kwargs = dict(kwargs)
            for _ in range(len(kwargs)):
                if "size" in kwargs:
                    self.width = kwargs["size"]
                    self.height = kwargs["size"]
                    del kwargs["size"]
                elif "x" in kwargs:
                    self.x = kwargs["x"]
                    del kwargs["x"]
                elif "y" in kwargs:
                    self.y = kwargs["y"]
                    del kwargs["y"]
                else:
                    self.id = kwargs["id"]
                    del kwargs["id"]
        if len(args) == 0 and len(copy_kwargs) == 0:
            return 1
        else:
            return 0

    def to_dictionary(self):
        """
        the class Rectangle by adding the public method

        def to_dictionary(self)

        that returns the dictionary representation of a Rectangle
        """
        new_dict = {}
        for i in range(len(self.__dict__) - 1):
            if i == 0:
                new_dict["x"] = self.x
            elif i == 1:
                new_dict["y"] = self.y
            elif i == 2:
                new_dict["size"] = self.size
            else:
                new_dict["id"] = self.id
        return new_dict
>>>>>>> 191e4a2018aa5ae4d7c78cb564c710d0c03342f9
