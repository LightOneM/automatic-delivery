import math


class abs_obj:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def distance_to(self, _obj):
        return math.sqrt((self.x - _obj.x) ** 2 + (self.y - _obj.y) ** 2) - self.radius - _obj.radius

    def x_distance_to(self, _obj):
        return _obj.x - self.x

    def y_distance_to(self, _obj):
        return _obj.y - self.y

    def collusion_with(self, _obj):
        if self.distance_to(_obj) <= 1: # not 0 because it will surpass it when moving and oscillate
            return True
        return False
