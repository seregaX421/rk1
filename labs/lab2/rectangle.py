from geometric_figure import GeometricFigure
from color import Color

class Rectangle(GeometricFigure):
    def __init__(self, width, height, color_name):
        self.width = width
        self.height = height
        self.color = Color(color_name)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f'Цвет: {self.color}, ширина: {self.width}, высота: {self.height}, площадь: {self.area}'

