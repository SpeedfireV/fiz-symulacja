import pygame
from pygame import Color, Rect
from pygame.font import Font
def text_input(screen, cursor_pos, text: str, color: Color, font: Font, rect_info: Rect, fill_color: Color, active:bool, entered_text:str):


    if active:
        text_color = Color(255, 255, 255)
        color = fill_color
    else:
        text_color = Color(255, 255, 255)
    if entered_text != "":
        text_surface = font.render(entered_text, True, text_color)
    else:
        text_surface = font.render(text, True, text_color)
    if active:
        color = Color(219, 178, 53)

    text_info = text_surface.get_rect().width, text_surface.get_rect().height
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge

        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=1000)
        screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                                   rect_info.y + rect_info.height / 2 - text_info[1] / 2])
        return True  # If Hovered

    else:
        if active:
            pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=1000)
        else:
            pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)



        screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                                   rect_info.y + rect_info.height / 2 - text_info[1] / 2])
        return False  # If Not Hovered