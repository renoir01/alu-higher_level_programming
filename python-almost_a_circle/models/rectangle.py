#!/usr/bin/python3
<<<<<<< HEAD
'''Defines a new class Rectangle which inherits from base
'''
=======
"""
the class Rectangle that inherits from Base

the file models/rectangle.py

Private instance attributes, each with its own public getter and setter

Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class.

With a setter, you are able to validate what a developer

is trying to assign to a variable.

So after, in your class you can “trust” these attributes.
"""


>>>>>>> 191e4a2018aa5ae4d7c78cb564c710d0c03342f9
from models.base import Base


class Rectangle(Base):
<<<<<<< HEAD
    '''Class Rectangle inherits from the Base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes new instances of Rectangle

        Args:
           width (int): Width of the rectangle to be initialized
           height (int):  Height of the rectangle to be initialized
           x (int): The horizontal position of the Rectangle
           y (int): The vertical position of the Rectangle.
           id (int): The id of the current class being initialized
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id})"
                f" {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    @property
    def width(self):
        '''Getter for width attribute
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''Setter for width attribute
        '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''Getter for height attribute
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''Setter for heigth attribute
        '''
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''Getter for x attribute
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''Setter for x attribute
        '''
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''Getter for y attribute
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''Setter for y attribute
        '''
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''Returns the area of the rectangle instance
        '''
        return self.__height * self.__width

    def display(self):
        '''Prints out a pictoral representation of the Rectangle instance
        '''
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        '''sets the instance attributes accoring to the variables store in args
        if args exists kwargs id skipped

        Args:
           args (no_keyword argument):
              1st argument should be the id attribute
              2nd argument should be the width attribute
              3rd argument should be the height attribute
              4th argument should be the x attribute
              5th argument should be the y attribute
           kwargs (keyword arguments):
              All keys and values have corresponding attributes
        '''
        if len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
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
                return value[12:]
            return value

        return {remove_prefix(key): self.__dict__[key]
                for key in self.__dict__.keys()}
=======
    """
    The class rectangle that has the

    Class constructor: def __init__(self, width, height, x=0, y=0, id=None)

    Private instance attributes, each with its own public getter and setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __width -> width

        __height -> height

        __x -> x

        __y -> y

        Calls the super class with id - this super call

        with use the logic of the __init__ of the Base class

        Assigns each argument width, height, x and y to the right attribute
        """
        try:
            self.width = width
            self.__width = width
        except Exception as e:
            raise
        try:
            self.height = height
            self.__height = height
        except Exception as e:
            raise
        try:
            self.x = x
            self.__x = x
        except Exception as e:
            raise
        try:
            self.y = y
            self.__y = y
        except Exception as e:
            raise
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"width must be an integer")
            elif value < 1:
                raise ValueError(f"width must be > 0")
            else:
                self.__width = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"height must be an integer")
            elif value < 1:
                raise ValueError(f"height must be > 0")
            else:
                self.__height = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"x must be an integer")
            elif value < 0:
                raise ValueError(f"x must be >= 0")
            else:
                self.__x = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"y must be an integer")
            elif value < 0:
                raise ValueError(f"y must be >= 0")
            else:
                self.__y = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    def __getattr__(self, name):
        if name == "width":
            pass
        elif name == "height":
            pass
        elif name == "x":
            pass
        elif name == "y":
            pass
        else:
            return None

    def area(self):
        """
        the public method def area(self):

        that returns the area value of the

        Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        the public method def display(self):

        that prints in stdout the Rectangle instance

        with the character #-

        not handling x and y here.

        now taking care of x and y

        in 7.display#1
        """
        shape = ""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            for _ in range(self.x):
                shape += " "
            for _ in range(self.width):
                shape += '#'
            if i != self.height - 1:
                shape += '\n'
        print(shape)
        return 0

    def __str__(self):
        """
        the class Rectangle by overriding the

        __str__ method so that it returns

        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        the public method def update(self, *args):

        that assigns an argument to each attribute

        1st argument should be the id attribute

        2nd argument should be the width attribute

        3rd argument should be the height attribute

        4th argument should be the x attribute

        5th argument should be the y attribute
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                else:
                    self.y = args[4]
        else:
            copy_kwargs = dict(kwargs)
            for _ in range(len(kwargs)):
                if "width" in kwargs:
                    self.width = kwargs["width"]
                    del kwargs['width']
                elif "height" in kwargs:
                    self.height = kwargs["height"]
                    del kwargs["height"]
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
        for i in range(len(self.__dict__)):
            if i == 0:
                new_dict["x"] = self.x
            elif i == 1:
                new_dict["y"] = self.y
            elif i == 2:
                new_dict["width"] = self.width
            elif i == 3:
                new_dict["height"] = self.height
            else:
                new_dict["id"] = self.id
        return new_dict
>>>>>>> 191e4a2018aa5ae4d7c78cb564c710d0c03342f9
