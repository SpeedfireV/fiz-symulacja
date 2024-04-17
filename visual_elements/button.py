import pygame
from pygame import Color, Rect
from pygame.font import Font


def render_text_button(screen, button_name, cursor_pos, text: str, color: Color, font: Font, rect_info: Rect):
    text_surface = font.render(text, True, Color(255, 255, 255))
    text_info = text_surface.get_rect().width, text_surface.get_rect().height
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
        screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                                   rect_info.y + rect_info.height / 2 - text_info[1] / 2])
        return button_name  # If Hovered

    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)
        screen.blit(text_surface, [rect_info.x + rect_info.width / 2 - text_info[0] / 2,
                                   rect_info.y + rect_info.height / 2 - text_info[1] / 2])
        return None  # If Not Hovered


def render_triangle_icon_button(screen, button_name, cursor_pos, color: Color, rect_info: Rect):
    rect_height = rect_info.height
    rect_width = rect_info.width
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))

        return button_name  # If Hovered

    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))

        return None  # If Not Hovered


def render_double_triangle_icon_button(screen, button_name, cursor_pos, color: Color, rect_info: Rect):
    rect_height = rect_info.height
    rect_width = rect_info.width
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 4, rect_info.y + rect_height / 2),))
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3 + 5, rect_info.y + rect_height / 2)))

        return button_name  # If Hovered

    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3 + 5, rect_info.y + rect_height / 2)))

        return None  # If Not Hovered


def render_inverted_triangle_icon_button(screen, button_name, cursor_pos, color: Color, rect_info: Rect):
    rect_height = rect_info.height
    rect_width = rect_info.width
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))

        return button_name  # If Hovered

    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))

        return None  # If Not Hovered


def render_inverted_double_triangle_icon_button(screen, button_name, cursor_pos, color: Color, rect_info: Rect):
    rect_height = rect_info.height
    rect_width = rect_info.width
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 4, rect_info.y + rect_height / 2),))
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3 + 5, rect_info.y + rect_height / 2)))

        return button_name  # If Hovered

    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))
        pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height / 3),
            (rect_info.x + rect_width / 3 + 5, rect_info.y + rect_height - rect_height / 3),
            (rect_info.x + rect_width - rect_width / 3 + 5, rect_info.y + rect_height / 2)))

        return None  # If Not Hovered


def render_stop_resume_icon_button(screen, button_name, cursor_pos, color: Color, rect_info: Rect, running: bool):
    rect_height = rect_info.height
    rect_width = rect_info.width
    button_maximums = [rect_info.x, rect_info.x + rect_info.width, rect_info.y, rect_info.y + rect_info.height]

    if (button_maximums[0] < cursor_pos[0] < button_maximums[1]) and (  # Cursor Between Left And Right Button's Edge
            button_maximums[2] < cursor_pos[1] < button_maximums[3]):  # Cursor Between Bottom And Top Button's Edge
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=100)
        if running:
            pygame.draw.line(screen, color=Color(255, 255, 255),
                             start_pos=(rect_info.x + rect_width / 4, rect_info.y + rect_height / 3),
                             end_pos=(rect_info.x + rect_width - rect_width / 4, rect_info.y + rect_height / 3),
                             width=3)
            pygame.draw.line(screen, color=Color(255, 255, 255),
                             start_pos=(rect_info.x + rect_width / 4, rect_info.y + rect_height - rect_height / 3),
                             end_pos=(
                             rect_info.x + rect_width - rect_width / 4, rect_info.y + rect_height - rect_height / 3),
                             width=3)
        else:
            pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
                (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
                (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
                (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))
        return button_name  # If Hovered

    else:
        pygame.draw.rect(surface=screen, color=color, rect=rect_info, width=3)
        if running:
            pygame.draw.line(screen, color=Color(255, 255, 255),
                             start_pos=(rect_info.x + rect_width / 4, rect_info.y + rect_height / 3),
                             end_pos=(rect_info.x + rect_width - rect_width / 4, rect_info.y + rect_height / 3),
                             width=3)
            pygame.draw.line(screen, color=Color(255, 255, 255),
                             start_pos=(rect_info.x + rect_width / 4, rect_info.y + rect_height - rect_height / 3),
                             end_pos=(
                                 rect_info.x + rect_width - rect_width / 4,
                                 rect_info.y + rect_height - rect_height / 3), width=3)
        else:
            pygame.draw.polygon(screen, color=Color(255, 255, 255), points=(
                (rect_info.x + rect_width / 3, rect_info.y + rect_height / 3),
                (rect_info.x + rect_width / 3, rect_info.y + rect_height - rect_height / 3),
                (rect_info.x + rect_width - rect_width / 3, rect_info.y + rect_height / 2),))
        return None  # If Not Hovered
