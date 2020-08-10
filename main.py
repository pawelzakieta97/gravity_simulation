import pygame
from point import Point
from body import Body
from engine import Engine
import math
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False

def draw(shape):
    if isinstance(shape, Point):
        pygame.draw.circle(screen, (0, 128, 255),
                           (int(shape.position[0]), int(shape.position[1]))
                           , int(math.sqrt(shape.m)), 1)
    if isinstance(shape, Body):
        for point in shape.points:
            draw(point)

p1 = Point(position=(400,100), mass=400)
p2 = Point(position=(400,110), mass=100)
# p3 = Point(position=(110,110))
# p4 = Point(position=(100,110))

p5 = Point(position=(400,400), mass=10000)
p6 = Point(position=(210,200))
p7 = Point(position=(210,210))
p8 = Point(position=(200,210))
body = Body()
body2 = Body()
body.add_points(p1,p2)
body2.add_points(p5)
# body.apply_impulse((100,0), (100,100))
body.v = np.array([5,0])
body2.v = np.array([-0.25, 0])
engine = Engine(body, body2)
# engine = Engine(body)
clock = pygame.time.Clock()
while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    engine.gravity()
    engine.update()
    for body in engine.bodies:
        draw(body)
    pygame.display.flip()
    print("orbiting body rotational vel.:", engine.bodies[0].w)
    clock.tick(60)