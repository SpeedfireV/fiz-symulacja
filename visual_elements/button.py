import pygame
from pygame import Color, Rect
from pygame.font import Font


def button(screen, cursor_pos, text: str, color: Color, font: Font, rect_info: Rect, function):
    text_surface = font.render(text, True, Color(255, 255, 255))

    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)

    text_info = text_surface.get_rect().width, text_surface.get_rect().height
    screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                               rect_info.y + rect_info.height / 2 - text_info[1] / 2])
