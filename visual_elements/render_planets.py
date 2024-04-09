import pygame
from pygame import Color

from objects.object import SpaceObject


def render_planets(screen,scale, objects: list[SpaceObject]):
    screen_center = screen.get_rect().center
    x_half_of_screen = screen_center[0]
    y_half_of_screen = screen_center[1]
    for object in objects:
        meters_per_pixel = abs(x_half_of_screen) / scale
        x_position = x_half_of_screen + meters_per_pixel * object.x
        y_position = y_half_of_screen - meters_per_pixel * object.y
        pygame.draw.circle(screen, Color(10, 190, 245), [x_position, y_position], radius=3)

