import math

import pygame
from pygame import Vector2, Color

from draw_vector import draw_vector

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True
i = 10
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(Color(20,20,20))
    draw_vector(screen=screen, start_pos=Vector2(100, 100), length=100, angle=7*math.pi/4)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    i += 1
    clock.tick(60)  # limits FPS to 60

pygame.quit()