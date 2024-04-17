import pygame
from pygame import Color

from buttons import return_buttons, render_text_simulation_speed
from calculate_geographical_position import calculate_geographical_position
from charts.distance_from_zero import draw_distance_from_zero
from entering_text import entering_numbers
from objects.simulation_controller import SimulationController
from objects.text_input_controller import TextInputController
from visual_elements.render_planets import render_planets
from visual_elements.scale_size import render_space_scale
from visual_elements.text_frame import render_text_frame

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
# Screen
display_info = pygame.display.Info()
screen_size = display_info.current_w - 1, display_info.current_h - 1
screen = pygame.display.set_mode(screen_size)
x_half_of_screen = screen.get_rect().center[0]
y_half_of_screen = screen.get_rect().center[1]
x_border = 0
y_border = 0
# Mouse
pygame.mouse.set_visible(False)
mouse_clicked = False
# Font Init
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 22)
# Simulation Tickrate
tickrate = 60
# Galaxy Scale
current_scale = 1_000
objects = []

364_397_000
text_controller = TextInputController()
simulation_speed_controller = SimulationController()
i = 1

distance_from_zero = {}

while running:
    cursor_pos = pygame.mouse.get_pos()
    x_cursor_pos, y_cursor_pos = cursor_pos[0], cursor_pos[1]

    geographical_x_position, geographical_y_position = calculate_geographical_position(screen, current_scale,
                                                                                       x_cursor_pos, y_cursor_pos,
                                                                                       x_border, y_border)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if text_controller.hovered is not None:
                    if text_controller.hovered == "*2x" or text_controller.hovered == "/2x" or text_controller.hovered == "double_increase_speed" or text_controller.hovered == "double_decrease_speed" or text_controller.hovered == "increase_speed" or text_controller.hovered == "decrease_speed" or text_controller.hovered == "stop_resume":
                        if text_controller.hovered == "*2x":
                            simulation_speed_controller.increase_double_speed()
                        elif text_controller.hovered == "/2x":
                            simulation_speed_controller.decrease_double_speed()
                        elif text_controller.hovered == "double_increase_speed":
                            simulation_speed_controller.double_increase_speed()
                        elif text_controller.hovered == "double_decrease_speed":
                            simulation_speed_controller.double_decrease_speed()
                        elif text_controller.hovered == "increase_speed":
                            simulation_speed_controller.increase_speed()
                        elif text_controller.hovered == "decrease_speed":
                            simulation_speed_controller.decrease_speed()
                        elif text_controller.hovered == "stop_resume":
                            if simulation_speed_controller.running:
                                simulation_speed_controller.running = False
                                draw_distance_from_zero(distance_from_zero)
                            else:
                                simulation_speed_controller.running = True

                    else:
                        # Submit Current State
                        text_controller.submit()
                        # Select New State
                        text_controller.select()
                else:
                    if text_controller.selected == 'select_position_x' or text_controller.select() == 'select_position_y':
                        text_controller.position_x_text = str(geographical_x_position)
                        text_controller.position_y_text = str(geographical_y_position)
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
                print("BACKSPACE")
                text_controller.backspace()
            elif event_key == pygame.K_ESCAPE:
                print("Escape Clicked")
            elif entering_numbers(event.unicode, event_key) is not None:
                text_controller.key_pressed(entering_numbers(event.unicode, event_key))

        if event.type == pygame.QUIT:
            running = False

    screen.fill(Color(20, 20, 20))

    # draw_vector(screen=screen, start_pos=Vector2(500, 500), length=100, angle=3*math.pi/2)
    render_text_frame(screen=screen, screen_size=screen_size, font=font, x_cursor_pos=cursor_pos[0],
                      y_cursor_pos=cursor_pos[1], geographical_x_position=geographical_x_position,
                      geographical_y_position=geographical_y_position)
    render_space_scale(screen=screen, x_screen_size=screen.get_rect().width, y_screen_size=screen.get_rect().height,
                       x_half_of_screen=x_half_of_screen, y_half_of_screen=y_half_of_screen, x_border=x_border,
                       y_border=y_border)
    is_clicked = pygame.mouse.get_pressed()[0]
    rect_pos = [screen_size[0] - 150, 10]
    rect_size = [140, 40]
    # Buttons
    buttons = return_buttons(screen=screen, cursor_pos=cursor_pos, screen_size=screen_size, font=font,
                             controller=text_controller, running=simulation_speed_controller.running)

    for button in buttons:
        if button is not None:
            text_controller.change_input(button)
            break
    else:
        text_controller.stopped_hovering()
    render_text_simulation_speed(screen=screen, font=font, simulation_speed=simulation_speed_controller.speed)
    if text_controller.selected == 'add_object' and text_controller.fulfilled:
        objects.append(text_controller.return_object())
        text_controller.reset()
    render_planets(screen=screen, font=font, scale=current_scale, objects=objects)
    pygame.draw.circle(screen, Color(10, 190, 245), cursor_pos, radius=5)

    render_text_simulation_speed(screen=screen, font=font, simulation_speed=simulation_speed_controller.speed)

    # Updates Screen !
    pygame.display.flip()
    if simulation_speed_controller.running:
        i += 1
        new_objects = []
        for pos, object in enumerate(objects):
            if distance_from_zero.get(object) is None:
                distance_from_zero[object] = [[object.x, i]]
            else:
                current_distances = distance_from_zero[object]
                current_distances.append([object.x, i])
                distance_from_zero[object] = current_distances
            new_object = object

            for other_object in objects[:pos] + objects[pos + 1:]:
                new_object.calculate_new_velocity(other_object, (tickrate * 100) / simulation_speed_controller.speed )

            new_objects.append(new_object)
        else:
            objects = new_objects
        for object in objects:
            object.change_position((tickrate * 100) / simulation_speed_controller.speed)
    clock.tick(tickrate)  # Limits FPS To The Maximum Tickrate

pygame.quit()
