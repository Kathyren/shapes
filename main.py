import sys
import os
from math import pi

class Circle:
    def __init__(self, radius, fill='red', stroke='black'):
        self._radius = radius # Private/protected
        self._fill = fill
        self._stroke = stroke
    @property
    def radius(self): #public access for radius READ ONLY
        return self._radius
    @property
    def are(self):
        return self.calculate_area()
    @property  # decorator
    def diameter(self):
        return self._radius*2

    def calculate_area(self):
        """
        Calculare the area
        :return:
        """
        return pi * self._radius ** 2
    def __len__(self):
        return int(2 * pi *self._radius) # using the private value

    def __call__(self):
        return "I am a happy circle c:"

    def __str__(self):
        return f"Circle radius {self._radius}, fill {self._fill}, stroke {self._stroke}"

    def __repr__(self):
        return f"Circle({self._radius}, {self._fill}, {self._stroke})"

def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"Area = {circle.calculate_area()}")
    circle2 = Circle(8.0) # default values
    print(f"area = {circle.are}")
    print(f"circunference is {len(circle)}")
    print(circle._radius)
    print(circle())

    print(repr(circle))
    print (circle)
    return 0


if __name__ == "__main__":
    sys.exit(main())
