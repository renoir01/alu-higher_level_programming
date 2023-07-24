#!/usr/bin/python3
'''Defines a class called Square'''


class Square:
    '''Square class represents a square'''

    def __init__(self, size=0):
        '''Initializes instances of Square.

           Args:
                size (int): Represents the size of one side of the square.
        '''
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
