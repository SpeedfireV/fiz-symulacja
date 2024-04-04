import math

import pygame
from pygame import Vector2, Color

from cursor_pos import draw_cursor_pos
from draw_vector import draw_vector
from scale_size import render_scale

# pygame setup
pygame.init()
display_info = pygame.display.Info()
screen_size = display_info.current_w - 1, display_info.current_h - 1
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(False)
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 30)
tickrate = 60
current_scale = 100
while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse Button Clicked!")
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    cursor_pos = pygame.mouse.get_pos()
    screen.fill(Color(20, 20, 20))
    pygame.draw.circle(screen, Color("red"), cursor_pos, radius=3)

    draw_vector(screen=screen, start_pos=Vector2(500, 500), length=100, angle=3*math.pi/2)
    draw_cursor_pos(screen=screen,screen_size=screen_size,font=font, cursor_pos=cursor_pos)
    render_scale(screen=screen, screen_size=screen_size, max_difference=100)
    is_clicked = pygame.mouse.get_pressed()[0]

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(tickrate)  # limits FPS to 60

pygame.quit()