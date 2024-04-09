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
    w1 = Worker("w1" ,width // 2, height // 3, 30, 9)
    w2 =Worker("w2", width // 2, height // 2, 30,  9)
    w3 =Worker("w3", width // 3, height // 2, 30, 9)
    workers = [w1,w3,w2]
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

        # todo implement some sort of sort and change the program to accept none type workers

        free_workers = []
        for w in workers:
            if w.occupiedby =="free" :
                free_workers.append(w)


        for w in workers:
            w.deliver()
            r_max_weight.call(w)
        # todo add call back list



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