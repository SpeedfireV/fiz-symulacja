from pygame import Rect, Color

from colors import delete_color, neutral_color, confirm_color
from objects.text_input_controller import TextInputController
from visual_elements.button import render_text_button, render_triangle_icon_button, render_double_triangle_icon_button, \
    render_stop_resume_icon_button
from visual_elements.text_input import text_input

def render_text_simulation_speed(screen, font, simulation_speed):
    if simulation_speed >= 100:
        simulation_speed =  str(simulation_speed)[-3::-1][::-1] + "." +  str(simulation_speed)[-1:-3:-1][::-1]
    text_surface = font.render(f'Sim. Speed: {simulation_speed}', True, (255, 255, 255))
    text_info = text_surface.get_rect().width, text_surface.get_rect().height
    screen.blit(text_surface, [screen.get_rect().width - 400 - text_info[0] / 2,
                               30 - text_info[1] / 2])

def return_buttons(screen, cursor_pos, screen_size, font, controller: TextInputController):
    return [
    render_text_button(screen=screen, button_name='clear_all', cursor_pos=cursor_pos, text="Clear All", color=delete_color, font=font,
                       rect_info=Rect(screen_size[0] - 150, 60, 140, 40)),
    render_text_button(screen=screen, button_name='add_object', cursor_pos=cursor_pos, text="Add Object",
                       color=confirm_color, font=font,
                       rect_info=Rect(screen_size[0] - 210, screen_size[1] - 60, 200, 50)),
    text_input(screen=screen, input_name='select_position_y', cursor_pos=cursor_pos, text="Select Position Y",
                   color=neutral_color, font=font,
                   rect_info=Rect(screen_size[0] - 210, screen_size[1] - 110, 200, 40), fill_color=Color(100, 100, 150),
                   active=controller.selected == "select_position_y", entered_text=controller.position_y_text),
    text_input(screen=screen, input_name='select_position_x', cursor_pos=cursor_pos, text="Select Position X",
               color=neutral_color, font=font,
               rect_info=Rect(screen_size[0] - 210, screen_size[1] - 160, 200, 40), fill_color=Color(100, 100, 150),
               active=controller.selected == "select_position_x", entered_text=controller.position_x_text),


    text_input(screen=screen, input_name='select_angle', cursor_pos=cursor_pos, text="Select Angle",
                   color=neutral_color, font=font,
                   rect_info=Rect(screen_size[0] - 210, screen_size[1] - 210, 200, 40), fill_color=Color(100, 100, 150),
                   active=controller.selected == "select_angle", entered_text=controller.angle_text),
    text_input(screen=screen, input_name='select_mass', cursor_pos=cursor_pos, text="Select Mass",
                  color=neutral_color, font=font,
                  rect_info=Rect(screen_size[0] - 210, screen_size[1] - 260, 200, 40), fill_color=Color(100, 100, 150),
                  active=controller.selected == "select_mass", entered_text=controller.mass_text),
    text_input(screen=screen, input_name='select_velocity', cursor_pos=cursor_pos, text="Select Velocity",
               color=neutral_color, font=font,
               rect_info=Rect(screen_size[0] - 210, screen_size[1] - 310, 200, 40),
               fill_color=Color(100, 100, 150), active=controller.selected == "select_velocity",
               entered_text=controller.velocity_text),

    text_input(screen=screen, input_name='select_name', cursor_pos=cursor_pos, text="Select Name",
                   color=neutral_color, font=font,
                   rect_info=Rect(screen_size[0] - 210, screen_size[1] - 360, 200, 40), fill_color=Color(100, 100, 150),
                   active=controller.selected == "select_name", entered_text=controller.name_text),
    render_text_button(screen=screen, button_name='*2x', cursor_pos=cursor_pos, text="*2x", color=Color(20, 60, 100), font=font,
                       rect_info=Rect(screen_size[0] - 210, 10, 40, 40)),
    render_double_triangle_icon_button(screen=screen, button_name='increase_speed', cursor_pos=cursor_pos,
                                           color=Color(20, 60, 100),
                                           rect_info=Rect(screen_size[0] - 260, 10, 40, 40)),
    render_triangle_icon_button(screen=screen, button_name='double_increase_speed', cursor_pos=cursor_pos,
                                color=Color(20, 60, 100),
                                rect_info=Rect(screen_size[0] - 310, 10, 40, 40)),
        render_text_button(screen=screen, button_name='/2x', cursor_pos=cursor_pos, text="/2x", color=Color(20, 60, 100),
                           font=font,
                           rect_info=Rect(screen_size[0] - 630, 10, 40, 40)),
        render_double_triangle_icon_button(screen=screen, button_name='decrease_speed', cursor_pos=cursor_pos,
                                           color=Color(20, 60, 100),
                                           rect_info=Rect(screen_size[0] - 580, 10, 40, 40)),
        render_triangle_icon_button(screen=screen, button_name='double_decrease_speed', cursor_pos=cursor_pos,
                                    color=Color(20, 60, 100),
                                    rect_info=Rect(screen_size[0] - 530, 10, 40, 40)),
        render_stop_resume_icon_button(screen=screen, button_name='stop_resume', cursor_pos=cursor_pos,
                                    color=Color(20, 60, 100),
                                    rect_info=Rect(screen_size[0] - 420, 60, 40, 40))





    ]
