import pygame.draw
from pygame import Color


def render_space_scale(screen, x_screen_size, y_screen_size, x_border, x_half_of_screen, y_half_of_screen, y_border):
    # X Scale
    pygame.draw.line(screen, color=Color(255, 255, 255), start_pos=[x_border, y_half_of_screen],
                     end_pos=[x_screen_size - x_border, y_half_of_screen])
    # Y Scale
    pygame.draw.line(screen, color=Color(255, 255, 255), start_pos=[x_half_of_screen, y_border],
                     end_pos=[x_half_of_screen, y_screen_size - y_border])
