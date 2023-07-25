#!/usr/bin/python3
'''Empty Rectangle class
'''


class Rectangle:
    '''
    Class represents a rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Initializes an new instance of the Rectangle class

        Args:
           width (int): The width of the rectangle instance
           height (int): The height of the rectangle instance
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Width getter

        Returns:
           The value of the width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width

        Args:
           value (int): The value to be stored as width
        '''
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for height

        Returns:
           The current value of height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height

         Args:
           value (int): The value to be stored in height
        '''
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
