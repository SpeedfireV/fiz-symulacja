import pygame
from pygame import Color

from objects.space_object import SpaceObject


def render_planets(screen, font, scale, objects: list[SpaceObject]):
    screen_center = screen.get_rect().center
    x_half_of_screen = screen_center[0]
    y_half_of_screen = screen_center[1]
    for object in objects:
        meters_per_pixel = abs(x_half_of_screen) / scale
        x_position = x_half_of_screen + meters_per_pixel * object.x
        y_position = y_half_of_screen - meters_per_pixel * object.y
        pygame.draw.circle(screen, object.color, [x_position, y_position], radius=3)
        text_surface = font.render(object.name, True, object.color)
        text_info = text_surface.get_rect().width, text_surface.get_rect().height
        screen.blit(text_surface, [x_position - text_info[0] / 2,
                                   y_position - text_info[1] / 2 - 20])


