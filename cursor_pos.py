import pygame.draw
from pygame import Color


def draw_cursor_pos(screen, font, cursor_pos):
    pygame.draw.rect(screen, color=Color('white'), rect=[1920 - 180, -1,1920,40], width=1)
    text_surface = font.render(f'{cursor_pos[0]}, {cursor_pos[1]}', False, (255, 255, 255))
    screen.blit(text_surface, (1920 - 160, 5))