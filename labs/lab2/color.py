class Color:
    def __init__(self, color_name):
        self.color_name = color_name

    @property
    def color_name(self):
        return self._color_name

    @color_name.setter
    def color_name(self, value):
        self._color_name = value
