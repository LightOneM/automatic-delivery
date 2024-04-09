from enum import Enum

from abstract_object import abs_obj
from settings import *


# state can be one of the following { "action" , "waiting" }

class Worker(abs_obj):
    def __init__(self, name, x, y, max_load, speed):
        super().__init__(x, y, WORKER_SIZE)
        self.name = name
        self.max_load = max_load
        self.speed = speed
        self.queue = []
        self.occupiedby = "free"

    def add_order(self, _order):
        self.queue.append(_order)

    def time_to_reach(self, _obj):
        return self.distance_to(_obj) / self.speed

    def time_to_finish(self):
        total_disatance = 0
        for i in range(0, len(self.queue) - 1):
            total_disatance += self.queue[i].distance_to(self.queue[i + 1])
        return total_disatance / self.speed

    def deliver(self):
        if self.queue:
            _order = self.queue[0]
            if self.collusion_with(_order):
                self.queue.pop(0)
            else:
                self.step_to(_order)
        if not self.queue and self.occupiedby=="delivery":
            self.occupiedby = "free"

    def to_restaurant(self, _rest):
        self.step_to(_rest)

    # todo add a limited step when close to the target
    def step_to(self, _obj):
        new_y = self.y + (self.speed * self.y_distance_to(_obj)) / self.distance_to(_obj)
        new_x = self.x + (self.speed * self.x_distance_to(_obj)) / self.distance_to(_obj)
        if 0 < new_x < WIDTH:
            self.x = new_x
        if 0 < new_y < HIGHT:
            self.y = new_y
