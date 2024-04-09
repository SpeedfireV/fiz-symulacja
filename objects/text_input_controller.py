from objects.object import SpaceObject


class TextInputController:
    def __init__(self):
        self.hovered = None
        self.selected = None
        self.fulfilled = False
        self.velocity_text = ""
        self.mass_text = ""
        self.angle_text = ""
        self.position_x_text = ""
        self.position_y_text = ""

    def change_input(self, newInput):
        self.hovered = newInput
    def stopped_hovering(self):
        self.hovered = None
    def key_pressed(self, key):
        key = str(key)
        if self.selected == 'select_velocity':
            self.velocity_text += key
        elif self.selected == 'select_mass':
            self.mass_text += key
        elif self.selected == 'select_angle':
            self.angle_text += key
        elif self.selected == 'select_position_x':
            self.position_x_text += key
        elif self.selected == 'select_position_y':
            self.position_y_text += key
    def backspace(self):
        if self.selected == 'select_velocity':
            self.velocity_text = self.velocity_text[:len(self.velocity_text) - 1]
        elif self.selected == 'select_mass':
            self.mass_text = self.mass_text[:len(self.mass_text) - 1]
        elif self.selected == 'select_angle':
            self.angle_text= self.angle_text[:len(self.angle_text) - 1]
        elif self.selected == 'select_position_x':
            self.position_x_text = self.position_x_text[:len(self.position_x_text) - 1]
        elif self.selected == 'select_position_y':
            self.position_y_text= self.position_y_text[:len(self.position_y_text) - 1]
    def submit(self):
        self.check_fulfilment()
        self.selected = None
    def select(self):
        self.selected = self.hovered

    def check_fulfilment(self):
        if self.mass_text != "" and self.angle_text != "" and self.velocity_text != "" and self.position_x_text != "" and self.position_y_text != "":
            self.fulfilled = True
        else:
            self.fulfilled = False

    def return_object(self):
        return SpaceObject(x=int(self.position_x_text), y=int(self.position_y_text), mass=float(self.mass_text), velocity=float(self.velocity_text),angle=float(self.angle_text))

    def reset(self):
        self.hovered = None
        self.selected = None
        self.fulfilled = False
        self.velocity_text = ""
        self.mass_text = ""
        self.angle_text = ""
        self.position_x_text = ""
        self.position_y_text = ""