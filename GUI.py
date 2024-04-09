import pygame
import random

from order import Order
from restaurant import Restaurant
from settings import *
from worker import Worker

pygame.init()
width, height = WIDTH, HIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fast_delivery")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)

def main():

    #trail = []  # Store positions of the player circle for trail effect
    w1 = Worker("w1" ,width // 2, height // 3, 30, 3)
    w3 =Worker("w1", width // 2, height // 2, 30,  3)
    w4 =Worker("w1", width // 3, height // 2, 30, 3)
    workers = [w1,w3,w4]
    r = Restaurant("r",width // 3,height // 2)
    restaurants = [r]
    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.random() < 0.012:
            rand_x = random.randint(0, width)
            rand_y = random.randint(0, height)
            r.add_order(Order(rand_x, rand_y, 1, 0))



        r_max_weight = restaurants[0]
        for r in restaurants:
            r_max_weight = r if r.get_restaurant_weight()>r_max_weight.get_restaurant_weight() else r_max_weight

        # todo implement some sort of sort and change the program to accept none type workers

        closest_worker = workers[0]
        for w in workers:
            w.deliver()
            if w.occupiedby is None:
                closest_worker = w if w.time_to_reach(r_max_weight)< closest_worker.time_to_reach(r_max_weight)else closest_worker
        r_max_weight.call(closest_worker)

        # trail.insert(0,(w1.x, w1.y))
        # if len(trail) > 21:
        #     trail.pop(len(trail)-1)


        if random.random() < 0.09:
            rand_x = random.randint(0, width)
            rand_y = random.randint(0, height)
            r.add_order(Order(rand_x,rand_y,1,0))


        screen.fill(WHITE)
        rest_orders = []
        for r in restaurants:
            rest_orders += r.orders
        work_orders = []
        for w in workers:
            work_orders += w.queue
        all_orders = rest_orders + work_orders
        for ord in all_orders:
            pygame.draw.circle(screen,BLUE , (ord.x, ord.y), ORDER_SIZE)

        # last = w1.radius
        # for index,pos in enumerate(trail):
        #     last = last * (3.8 / 4.0)
        #     pygame.draw.circle(screen, GREEN, pos,last)

        for w in workers:
            pygame.draw.circle(screen, GREEN, (w.x, w.y), WORKER_SIZE)
        for r in restaurants:
            pygame.draw.circle(screen, RED, (r.x, r.y), RESTAURANT_SIZE)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()