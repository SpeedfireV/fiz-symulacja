

class TextInputController:
    def __init__(self):
        self.selected = None
        self.velocity_text = ""
        self.mass_text = ""
        self.angle_text = ""
        self.position_x_text = ""
        self.position_y_text = ""

    def change_input(self, newInput):
        self.selected = newInput
    def end_input(self):
        self.selected = None
    def key_pressed(self, key):
        if self.selected == 'velocity':
            self.velocity_text += key
        elif self.selected == 'mass':
            self.mass_text += key
        elif self.selected == 'angle':
            self.angle_text += key
        elif self.selected == 'position_x':
            self.position_x_text += key
        elif self.selected == 'position_y':
            self.position_y_text += key
