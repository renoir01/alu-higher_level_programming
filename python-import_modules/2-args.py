#!/usr/bin/python3
import sys
if __name__ == "__main__":
    def args():
        length = len(sys.argv)
        if length == 1:
            print("{0:d} arguments.".format(length - 1))
            return 1

        if length == 2:
            print("{0:d} argument:".format(length - 1))
        else:
            print("{0:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{0:d}: {1:s}".format(i, sys.argv[i]))
        return 0
    args()
