import pygame.draw
from pygame import Color, Rect
from pygame.font import Font


def render_text_frame(screen, scale, screen_size, font: Font,x_cursor_pos, y_cursor_pos):
    screen_center = screen.get_rect().center
    x_half_of_screen = screen_center[0]
    y_half_of_screen = screen_center[1]
    meters_per_pixel = abs(x_half_of_screen) / scale

    rect_pos = [screen_size[0] - 150, 10]
    rect_size = [140, 40]
    rect_info = Rect(rect_pos[0], rect_pos[1], rect_size[0], rect_size[1])
    pygame.draw.rect(screen, color=Color('white'), rect=rect_info, width=3)
    text_surface = font.render(f'{x_cursor_pos}, {y_cursor_pos}', True, (255, 255, 255))
    text_info = text_surface.get_rect().width, text_surface.get_rect().height
    screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                               rect_info.y + rect_info.height / 2 - text_info[1] / 2])
    text_surface = font.render(f'{int((x_cursor_pos - x_half_of_screen) / meters_per_pixel)}, {int((y_half_of_screen - y_cursor_pos)/ meters_per_pixel)}', True, (255, 255, 255))
    text_info = text_surface.get_rect().width, text_surface.get_rect().height
    screen.blit(text_surface, [x_half_of_screen - text_info[0] / 2,
                               10])
