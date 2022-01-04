class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class Box:

    def __init__(self, x, y, color=Color(0, 100, 100), width=1, height=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def __repr__(self):
        return f'({self.x}, {self.y}) [{self.width}, {self.height}]'
