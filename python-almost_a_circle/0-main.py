#!/usr/bin/python3
""" 0-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    # Test cases for Base class
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

    # Test cases for Rectangle class
    r1 = Rectangle(2, 3)
    print(r1.id)
    r2 = Rectangle(4, 5, 1, 2, 6)
    print(r2.id)

    # Test cases for Square class
    s1 = Square(5)
    print(s1.id)
    s2 = Square(7, 2, 3, 8)
    print(s2.id)
