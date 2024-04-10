from pygame import Rect, Color

from colors import delete_color, neutral_color, confirm_color
from objects.text_input_controller import TextInputController
from visual_elements.button import render_button
from visual_elements.text_input import text_input


def return_buttons(screen, cursor_pos, screen_size, font, controller: TextInputController):
    return [
    render_button(screen=screen,button_name='clear_all', cursor_pos=cursor_pos, text="Clear All", color=delete_color, font=font,
                                         rect_info=Rect(screen_size[0] - 150, 60, 140, 40)),
    render_button(screen=screen, button_name='add_object',cursor_pos=cursor_pos, text="Add Object",
                                                  color=confirm_color, font=font,
                                                  rect_info=Rect(screen_size[0] - 210, screen_size[1] - 80, 200, 50)),
        text_input(screen=screen, input_name='select_position_y', cursor_pos=cursor_pos, text="Select Position Y",
                   color=neutral_color, font=font,
                   rect_info=Rect(screen_size[0] - 210, screen_size[1] - 140, 200, 40), fill_color=Color(100, 100, 150),
                   active=controller.selected == "select_position_y", entered_text=controller.position_y_text),
    text_input(screen=screen, input_name='select_position_x', cursor_pos=cursor_pos, text="Select Position X",
               color=neutral_color, font=font,
               rect_info=Rect(screen_size[0] - 210, screen_size[1] - 190, 200, 40), fill_color=Color(100, 100, 150),
               active=controller.selected == "select_position_x", entered_text=controller.position_x_text),


    text_input(screen=screen, input_name='select_angle', cursor_pos=cursor_pos, text="Select Angle",
                   color=neutral_color, font=font,
                   rect_info=Rect(screen_size[0] - 210, screen_size[1] - 240, 200, 40), fill_color=Color(100, 100, 150),
                   active=controller.selected == "select_angle", entered_text=controller.angle_text),
    text_input(screen=screen, input_name='select_mass', cursor_pos=cursor_pos, text="Select Mass",
                  color=neutral_color, font=font,
                  rect_info=Rect(screen_size[0] - 210, screen_size[1] - 290, 200, 40), fill_color=Color(100, 100, 150),
                  active=controller.selected == "select_mass", entered_text=controller.mass_text),
    text_input(screen=screen, input_name='select_velocity', cursor_pos=cursor_pos, text="Select Velocity",
               color=neutral_color, font=font,
               rect_info=Rect(screen_size[0] - 210, screen_size[1] - 340, 200, 40),
               fill_color=Color(100, 100, 150), active=controller.selected == "select_velocity",
               entered_text=controller.velocity_text),

    text_input(screen=screen, input_name='select_name', cursor_pos=cursor_pos, text="Select Name",
                   color=neutral_color, font=font,
                   rect_info=Rect(screen_size[0] - 210, screen_size[1] - 390, 200, 40), fill_color=Color(100, 100, 150),
                   active=controller.selected == "select_name", entered_text=controller.name_text),

    ]