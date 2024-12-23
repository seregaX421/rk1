import math
from geometric_figure import GeometricFigure
from color import Color

class Circle(GeometricFigure):
    def __init__(self, radius, color_name):
        self.radius = radius
        self.color = Color(color_name)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Circle(color: {}, radius: {}, area: {:.1f})".format(
            self.color.color_name, self.radius, self.area()
        )
