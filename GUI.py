import pygame
import random

from order import Order
from restaurant import Restaurant
from settings import WIDTH, HIGHT
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

    trail = []  # Store positions of the player circle for trail effect
    w1 = Worker("w1" ,width // 2, height // 2, 30, 5)
    r = Restaurant("r",width // 3,height // 2)
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


        if w1.state =="waiting":
            w1.to_restaurant(r)
            r.load(w1)
        w1.deliver()

        trail.insert(0,(w1.x, w1.y))
        if len(trail) > 21:
            trail.pop(len(trail)-1)


        if random.random() < 0.001:
            rand_x = random.randint(0, width)
            rand_y = random.randint(0, height)
            r.add_order(Order(rand_x,rand_y,1,0))


        screen.fill(WHITE)

        for ord in r.orders:
            pygame.draw.circle(screen,BLUE , (ord.x, ord.y), ord.radius)
        for ord in w1.queue:
            pygame.draw.circle(screen, BLUE, (ord.x, ord.y), ord.radius)

        last = w1.radius
        for index,pos in enumerate(trail):
            last = last * (3.8 / 4.0)
            pygame.draw.circle(screen, GREEN, pos,last)


        pygame.draw.circle(screen, GREEN, (w1.x, w1.y), w1.radius)
        pygame.draw.circle(screen, RED, (r.x, r.y), r.radius)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()