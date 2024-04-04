import math

from pygame import Color, Vector2
from pygame.draw import line


def draw_vector(screen, start_pos, length, angle): # (length^2)/2 = x^2
    x = math.cos(angle) * length
    y = math.sin(angle) * length
    end_pos = Vector2(start_pos.x + x, start_pos.y - y)
    line(surface=screen, color=Color(255, 255, 255), start_pos=start_pos,
                     end_pos=end_pos, width=1)

    arrow_1_angle = -(angle - math.pi/6 + math.pi)
    arrow_2_angle = -(angle + math.pi / 6 + math.pi)

    arrow_1_x = math.cos(arrow_1_angle) * 20
    arrow_1_y = math.sin(arrow_1_angle) * 20
    arrow_2_x = math.cos(arrow_2_angle) * 20
    arrow_2_y = math.sin(arrow_2_angle) * 20

    arrow_1_end = Vector2(end_pos.x + arrow_1_x, end_pos.y + arrow_1_y)
    arrow_2_end = Vector2(end_pos.x + arrow_2_x, end_pos.y + arrow_2_y)

    line(surface=screen, color=Color(255, 255, 255), start_pos=end_pos,
         end_pos=arrow_1_end, width=1)
    line(surface=screen, color=Color(255, 255, 255), start_pos=end_pos,
         end_pos=arrow_2_end, width=1)