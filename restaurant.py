from abstract_object import abs_obj
from settings import *


class Restaurant(abs_obj):
    def __init__(self, name, x, y):
        super().__init__(x, y, RESTAURANT_SIZE)
        self.name = name
        self.orders = []

    def add_order(self, _order):
        self.orders.append(_order)

    def delete_order(self, _order):
        self.orders.remove(_order)

    def load(self, _worker):
        for _order in self.orders:
            self.orders.remove(_order)
            _worker.add_order(_order)

    def get_restaurant_weight(self):
        return len(self.orders)


    def call(self,_worker):
        if _worker.occupiedby =="free":
            _worker.occupiedby = self.name
        if _worker.occupiedby == self.name:
            _worker.to_restaurant(self)
            if self.collusion_with(_worker):
                _worker.occupiedby = "delivery"
                self.load(_worker)

