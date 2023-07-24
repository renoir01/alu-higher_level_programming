#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Square represents an instance of a square shape'''

    def __init__(self, size=0):
        '''Initializes a new square object

           Args:
                size (int): The size of the square.
        '''
        self.size = size

    def area(self):
        '''
           Computes the area of the square based on the size.

           Returns:
               The value of the area (int).
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
           Retrieves the value of size
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
           Sets the value of private attribute size
        '''
        if (type(value) != int and type(value) != float):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, inst):
        '''
        Allows for == comparison between instances

        Args:
           cmp (Square): The instance being compared against
        '''
        return (self.area() == inst.area())

    def __lt__(self, inst):
        '''
        Allows < comparison between instances of this class

        Args:
           inst (Square): The instance being compared against
        '''
        return (self.area() < inst.area())

    def __le__(self, inst):
        '''
        Allows <= comparison between instances of this class

        Args:
           inst (Square): The instance being compared against
        '''
        return (self.area() <= inst.area())
