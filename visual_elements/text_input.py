import pygame
from pygame import Color, Rect
from pygame.font import Font


def text_input(screen, input_name, cursor_pos, text: str, color: Color, font: Font, rect_info: Rect, fill_color: Color,
               active: bool, entered_text: str):
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]
    hovered =  (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (
            button_maximums[2] < cursor_pos[1] < button_maximums[3])
    if active:
        text_color = Color(255, 255, 255)
        color = fill_color
    elif hovered:
        text_color = Color(100, 100, 50)
    else:
        text_color = Color(255, 255, 255)
    if entered_text != "":
        text_surface = font.render(entered_text, True, text_color)
    else:
        text_surface = font.render(text, True, text_color)
    if active:
        color = Color(219, 178, 53)

    text_info = text_surface.get_rect().width, text_surface.get_rect().height

    if hovered:  # Cursor Between Bottom And Top Button's Edge

        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=1000)
        screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                                   rect_info.y + rect_info.height / 2 - text_info[1] / 2])
        return input_name  # If Hovered

    else:
        if active:
            pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=1000)
        else:
            pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)

        screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                                   rect_info.y + rect_info.height / 2 - text_info[1] / 2])
        return None  # If Not Hovered
