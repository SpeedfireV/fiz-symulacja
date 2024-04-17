from objects.space_object import SpaceObject


class TextInputController:
    def __init__(self):
        self.hovered = None
        self.selected = None
        self.fulfilled = False
        self.name_text = ""
        self.velocity_text = ""
        self.scale_velocity_text = ""
        self.mass_text = ""
        self.scale_mass_text = ""
        self.angle_text = ""
        self.position_x_text = ""
        self.scale_position_x_text = ""
        self.position_y_text = ""
        self.scale_position_y_text = ""

    def change_input(self, newInput):
        self.hovered = newInput
    def stopped_hovering(self):
        self.hovered = None
    def key_pressed(self, key):
        key = str(key)
        if self.selected == 'select_velocity':
            self.velocity_text += key
        elif self.selected == 'select_scale_velocity':
            self.scale_velocity_text += key
        elif self.selected == 'select_mass':
            self.mass_text += key
        elif self.selected == 'select_scale_mass':
            self.scale_mass_text += key
        elif self.selected == 'select_angle':
            self.angle_text += key
        elif self.selected == 'select_position_x':
            self.position_x_text += key
        elif self.selected == 'select_scale_position_x':
            self.scale_position_x_text += key
        elif self.selected == 'select_position_y':
            self.position_y_text += key
        elif self.selected == 'select_scale_position_y':
            self.scale_position_y_text += key
        elif self.selected == 'select_name':
            self.name_text += key

    def backspace(self):
        if self.selected == "select_name":
            self.name_text = self.name_text[:len(self.name_text) - 1]
        elif self.selected == 'select_velocity':
            self.velocity_text = self.velocity_text[:len(self.velocity_text) - 1]
        elif self.selected == "select_scale_velocity":
            self.scale_velocity_text = self.scale_velocity_text[:len(self.scale_velocity_text) - 1]
        elif self.selected == 'select_mass':
            self.mass_text = self.mass_text[:len(self.mass_text) - 1]
        elif self.selected == "select_scale_mass":
            self.scale_mass_text = self.scale_mass_text[:len(self.scale_mass_text) - 1]
        elif self.selected == 'select_angle':
            self.angle_text= self.angle_text[:len(self.angle_text) - 1]

        elif self.selected == 'select_position_x':
            self.position_x_text = self.position_x_text[:len(self.position_x_text) - 1]
        elif self.selected == "select_scale_position_x":
            self.scale_position_x_text = self.scale_position_x_text[:len(self.scale_position_x_text) - 1]
        elif self.selected == 'select_position_y':
            self.position_y_text= self.position_y_text[:len(self.position_y_text) - 1]
        elif self.selected == "select_scale_position_y":
            self.scale_position_y_text = self.scale_position_y_text[:len(self.scale_position_y_text) - 1]
    def submit(self):
        self.check_fulfilment()
        self.selected = None
    def select(self):
        self.selected = self.hovered

    def check_fulfilment(self):
        if self.name_text != "" and self.mass_text != "" and self.angle_text != "" and self.velocity_text != "" and self.position_x_text != "" and self.position_y_text != "":
            self.fulfilled = True
        else:
            self.fulfilled = False

    def return_object(self):
        if self.scale_position_x_text != "":
            x_scale = int(self.scale_position_x_text)
        else:
            x_scale = 0
        if self.scale_position_y_text != "":
            y_scale = int(self.scale_position_y_text)
        else:
            y_scale = 0
        if self.scale_velocity_text != "":
            velocity_scale = int(self.scale_velocity_text)
        else:
            velocity_scale = 0
        if self.scale_mass_text != "":
            mass_scale = int(self.scale_mass_text)
        else:
            mass_scale = 0
        return SpaceObject(name=self.name_text, x=int(self.position_x_text) * 10 ** x_scale, y=int(self.position_y_text) * 10 ** y_scale, mass=float(self.mass_text) * 10 ** mass_scale, velocity=float(self.velocity_text) * 10 ** velocity_scale,angle=float(self.angle_text))

    def reset(self):
        self.hovered = None
        self.selected = None
        self.fulfilled = False
        self.name_text = ""
        self.velocity_text = ""
        self.mass_text = ""
        self.angle_text = ""
        self.position_x_text = ""
        self.position_y_text = ""
