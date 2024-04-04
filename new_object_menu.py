import pygame.draw
from pygame import Color, Rect


def menu_create_object(screen, screen_size, cursor_pos):
    rect_pos = [cursor_pos[0],cursor_pos[1]]
    rect_size = [100,100]
    rect_info = Rect(rect_pos[0], rect_pos[1], rect_size[0], rect_size[1])
    pygame.draw.rect(screen,Color(255,255,255), rect_info, width=4)
