import math

import pygame
from pygame import Color, Rect, Vector2

from buttons import return_buttons
from entering_text import entering_numbers
from objects.object import calculate_cartesian_velocities
from objects.text_input_controller import TextInputController
from visual_elements.button import render_button
from visual_elements.text_frame import render_text_frame
from visual_elements.draw_vector import draw_vector
from visual_elements.new_object_menu import menu_create_object
from visual_elements.scale_size import render_scale
from colors import confirm_color, delete_color, neutral_color
from visual_elements.text_input import text_input

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
# Screen
display_info = pygame.display.Info()
screen_size = display_info.current_w - 1, display_info.current_h - 1
screen = pygame.display.set_mode(screen_size)
# Mouse
pygame.mouse.set_visible(False)
mouse_clicked = False
# Font Init
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 24)
# Simulation Tickrate
tickrate = 180
# Galaxy Scale
current_scale = 100
# Menu
menu_opened = False
menu_position = []
# Buttons Info
add_object_button_hovered = False
clear_button_hovered = False
editing = False

timer = 0

text_controller = TextInputController()
hovering_button = ""
while running:
    cursor_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                menu_opened = True
                menu_position = cursor_pos
                mouse_clicked = True
                if add_object_button_hovered:
                    print("Add Object")
                elif clear_button_hovered:
                    print("Clear Objects")
        else:
            mouse_clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                text_controller.end_input()
                print("Enter Clicked")
            elif event.key == pygame.K_BACKSPACE:
                print("Backspace Clicked")
            elif event.key == pygame.K_ESCAPE:
                print("Escape Clicked")


        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color(20, 20, 20))

    # draw_vector(screen=screen, start_pos=Vector2(500, 500), length=100, angle=3*math.pi/2)
    render_text_frame(screen=screen, screen_size=screen_size, font=font, text=f'{cursor_pos[0]}, {cursor_pos[1]}')
    render_scale(screen=screen, screen_size=screen_size, max_difference=100)
    is_clicked = pygame.mouse.get_pressed()[0]
    rect_pos = [screen_size[0] - 150, 10]
    rect_size = [140, 40]
    # Buttons
    buttons = return_buttons(screen=screen, cursor_pos=cursor_pos, screen_size=screen_size, font=font, controller=text_controller)

    for button in buttons:
        if button is not None:
            text_controller.change_input(button)
            break

    if menu_opened:
        menu_create_object(screen=screen, screen_size=screen_size, cursor_pos=menu_position)
    else:
        pass

    pygame.draw.circle(screen, Color(10, 190, 245), cursor_pos, radius=5)
    # Updates Screen !
    pygame.display.flip()
    clock.tick(tickrate)  # Limits FPS To The Maximum Tickrate
    print(text_controller.selected)

pygame.quit()
