import pygame
from pygame import Color

from buttons import return_buttons
from entering_text import entering_numbers
from objects.text_input_controller import TextInputController
from visual_elements.render_planets import render_planets
from visual_elements.scale_size import render_scale
from visual_elements.text_frame import render_text_frame

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
current_scale = 100000
objects = []

text_controller = TextInputController()
while running:
    cursor_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if text_controller.hovered is not None:
                    # Submit Current State
                    text_controller.submit()
                    # Select New State
                    text_controller.select()
                else:
                    text_controller.submit()

                if text_controller.selected == 'clear_all':
                    objects = []


        else:
            mouse_clicked = False
        if event.type == pygame.KEYDOWN:
            event_key = event.key
            if event_key == pygame.K_RETURN or event_key == pygame.K_SPACE:
                text_controller.submit()
            elif event_key == pygame.K_BACKSPACE:
                text_controller.backspace()
            elif event_key == pygame.K_ESCAPE:
                print("Escape Clicked")
            elif entering_numbers(event_key) is not None:
                text_controller.key_pressed(entering_numbers(event_key))

        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color(20, 20, 20))


    # draw_vector(screen=screen, start_pos=Vector2(500, 500), length=100, angle=3*math.pi/2)
    render_text_frame(screen=screen, scale=current_scale,screen_size=screen_size, font=font, x_cursor_pos=cursor_pos[0], y_cursor_pos=cursor_pos[1])
    render_scale(screen=screen, screen_size=screen_size, max_difference=100)
    is_clicked = pygame.mouse.get_pressed()[0]
    rect_pos = [screen_size[0] - 150, 10]
    rect_size = [140, 40]
    # Buttons
    buttons = return_buttons(screen=screen, cursor_pos=cursor_pos, screen_size=screen_size, font=font,
                             controller=text_controller)

    for button in buttons:
        if button is not None:
            text_controller.change_input(button)
            break
    else:
        text_controller.stopped_hovering()

    if text_controller.selected == 'add_object' and text_controller.fulfilled:
        objects.append(text_controller.return_object())
        text_controller.reset()
    render_planets(screen=screen, font=font, scale=current_scale, objects=objects)
    pygame.draw.circle(screen, Color(10, 190, 245), cursor_pos, radius=5)
    # Updates Screen !
    pygame.display.flip()
    new_objects = []
    for object in objects:
        new_object = object
        new_object.change_position(tickrate)
        new_objects.append(new_object)
    else:
        objects = new_objects

    clock.tick(tickrate)  # Limits FPS To The Maximum Tickrate

pygame.quit()
