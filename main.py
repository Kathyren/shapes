import sys
import os
from math import pi
import yaml


class Canvas:
    def __init__(self, width=10, height=10, bg='white'):
        self.width = width
        self.height = height
        self.bg = bg


class Text:
    def __init__(self, font="Arial", size=20, color="black"):
        self.font = font
        self.size = size
        self.color = color


class Circle:
    def __init__(self, radius, fill='red', stroke='black', at=(0, 0)):
        self._radius = radius  # Private/protected
        self._fill = fill
        self._stroke = stroke
        self._at = at

    @property
    def radius(self):  # public access for radius READ ONLY
        return self._radius

    @property
    def are(self):
        return self.calculate_area()

    @property  # decorator
    def diameter(self):
        return self._radius * 2

    def calculate_area(self):
        """
        Calculare the area
        :return:
        """
        return pi * self._radius ** 2

    def __len__(self):
        return int(2 * pi * self._radius)  # using the private value

    def __call__(self):
        return "I am a happy circle c:"

    def __str__(self):
        string = {
            'circle': {
                'radius': self.radius,
                'fill': self._fill,
                'stroke': self._stroke,
                'at': self._at
            }
        }
        string = yaml.dump(string)
        return string
    @classmethod
    def from_yaml(cls, string):
        """create circle from yaml str"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj

    def __repr__(self):
        return f"Circle({self._radius}, {self._fill}, {self._stroke})"


class Stroke:
    def __init__(self, width=1, color="red"):
        self.width = width
        self.color = color


class Quadrilateral:
    def __init__(self, line=Stroke(), fill='pink', width=1, height=1):
        """
        :param line:
        :param fill:
        :param width:
        :param height:
        """
        self.stroke = line
        self.fill = fill
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"Area = {circle.calculate_area()}")
    print(f"area = {circle.are}")
    print(f"circunference is {len(circle)}")
    print(circle._radius)
    print(circle())

    print(repr(circle))
    print(circle)
    yaml_circle = """\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red
    """
    my_circle = Circle.from_yaml(yaml_circle)



    return 0


if __name__ == "__main__":
    sys.exit(main())
