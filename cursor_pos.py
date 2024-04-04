import pygame.draw
from pygame import Color


def draw_cursor_pos(screen, screen_size, font, cursor_pos):
    pygame.draw.rect(screen, color=Color('white'), rect=[screen_size[0] - 180, -1,screen_size[0],40], width=1)
    text_surface = font.render(f'{cursor_pos[0]}, {cursor_pos[1]}', False, (255, 255, 255))
    screen.blit(text_surface, (screen_size[0] - 160, 5))