#!/usr/bin/env python3

import sys

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.repaired = False

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer", file=sys.stdout)
        else:
            self._size = value

    def cobble(self):
        self.repaired = True
        print("Your shoe is as good as new!\n")
