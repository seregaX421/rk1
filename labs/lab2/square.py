from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color_name):
        super().__init__(side, side, color_name)

    def __repr__(self):
        return f"Square(color: {self.color.color_name}, side: {self.width}, area: {self.area()})"
