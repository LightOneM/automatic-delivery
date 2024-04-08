from abstract_object import abs_obj
from settings import *


class Order(abs_obj):
    def __init__(self, x, y,weight,time):
        super().__init__(x, y, ORDER_SIZE)
        self.weight = weight
        self.time = time


