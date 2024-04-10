
def calculate_geographical_position(screen, current_scale, x_cursor_pos, y_cursor_pos, x_border, y_border):
    x_half_of_screen = screen.get_rect().center[0] - x_border
    y_half_of_screen = screen.get_rect().center[1] - y_border
    meters_per_pixel = abs(x_half_of_screen) / current_scale


    return int((x_cursor_pos - x_half_of_screen - x_border) / meters_per_pixel), int((y_half_of_screen - y_cursor_pos + y_border) / meters_per_pixel)
