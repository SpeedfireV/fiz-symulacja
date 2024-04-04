import pygame
from pygame import Color, Rect

from visual_elements.button import button
from visual_elements.cursor_pos import draw_cursor_pos
from visual_elements.new_object_menu import menu_create_object
from visual_elements.scale_size import render_scale
from colors import confirm_color

# pygame setup
pygame.init()
display_info = pygame.display.Info()
screen_size = display_info.current_w - 1, display_info.current_h - 1
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(False)
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 24)
tickrate = 180
current_scale = 100
objects = []
menu_opened = False
menu_position = []
while running:
    cursor_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print("Left Mouse Button Clicked!")
                menu_opened = True
                menu_position = cursor_pos

        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color(20, 20, 20))

    # draw_vector(screen=screen, start_pos=Vector2(500, 500), length=100, angle=3*math.pi/2)
    draw_cursor_pos(screen=screen, screen_size=screen_size, font=font, cursor_pos=cursor_pos)
    render_scale(screen=screen, screen_size=screen_size, max_difference=100)
    is_clicked = pygame.mouse.get_pressed()[0]
    rect_pos = [screen_size[0] - 150, 10]
    rect_size = [140, 40]
    button(screen=screen, cursor_pos=cursor_pos, text="Clear All", color=confirm_color, font=font,
           rect_info=Rect(screen_size[0] - 150, 60, 140, 40), function="")

    if menu_opened:
        menu_create_object(screen=screen, screen_size=screen_size, cursor_pos=menu_position)
    else:
        pass

    pygame.draw.circle(screen, Color(10, 190, 245), cursor_pos, radius=5)
    # Updates Screen !
    pygame.display.flip()
    clock.tick(tickrate)  # limits FPS to 60

pygame.quit()
