from enum import Enum


class PLocation(Enum):
    BOT_LEFT = 0
    BOT_RIGHT = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3


class Box:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = [Point((x * 2), (y * 2)),
                       Point((x * 2) + 1, (y * 2)),
                       Point((x * 2), (y * 2) + 1),
                       Point((x * 2) + 1, (y * 2) + 1)]

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connections = []

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def get_box_index(self):
        return self.x // 2, self.y // 2

    def connect_to(self, other_point):
        self.connections.append(other_point)
        other_point.connections.append(self)

    def is_connected_to(self, other_point):
        return other_point in self.connections
