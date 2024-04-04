import pygame.draw
from pygame import Color


def render_scale(screen,screen_size, max_difference):
    pygame.draw.line(screen, color=Color(255,255,255),start_pos=[screen_size[0]/2, 10], end_pos=[screen_size[0]/2,screen_size[1] - 10])
    pygame.draw.line(screen, color=Color(255,255,255),start_pos=[10, screen_size[1]/2], end_pos=[screen_size[0] - 10, screen_size[1]/2])