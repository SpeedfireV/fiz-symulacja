import math

from scipy.constants import gravitational_constant
from math import cos, sin, atan, sqrt


def calculate_cartesian_velocities(velocity, angle):
    x_velocity = velocity * cos(angle)
    y_velocity = velocity * sin(angle)
    return x_velocity, y_velocity

def calculate_by_distance_angle(x, y):
    if x == 0:
        if y > 0:
            return 0.5 * math.pi
        else:
            return 1.5 * math.pi
    elif y == 0:
        if x < 0:
            return math.pi
        else:
            return 0
    tangens = y / x
    angle = math.atan(tangens)

    if x > 0 and y > 0: # I
        pass
    elif x < 0 and y > 0: # II

        angle = math.pi + angle
    elif x < 0 and y < 0: # III

        angle = math.pi + angle
    elif x > 0 and y < 0: # IV

        angle = 2 * math.pi + angle
    while angle > math.pi * 2:
        angle -= 2 * math.pi
    return angle
def calculate_two_point_angle(first_point, second_point):
    x = second_point[0] - first_point[0]
    y = second_point[1] - first_point[1]
    return calculate_by_distance_angle(x,y)

# print(calculate_by_distance_angle(-50,-100))



class SpaceObject:
    def __init__(self, name: str, x: float, y: float, mass: float, velocity: float, angle: float):
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.angle = angle * math.pi
        self.G = gravitational_constant

    def __str__(self):
        return (f"Coordinates of {self.name}: {self.x} x {self.y}, the mass is equal to {self.mass}, the velocity is {self.velocity}"
                f" and the angle is {self.angle} pi")

    def calculate_distance(self, other_object):
        return math.sqrt((self.x - other_object.x) ** 2 + (self.y - other_object.y) ** 2)
    def calculate_new_velocity(self, other_object, fps: int):
        distance = self.calculate_distance(other_object)
        if distance < 1:
            return None
        acceleration = (self.G * other_object.mass) / pow(distance, 2)  # a = GM/R^2
        added_velocity = acceleration * (1 / fps)  # [a] = m/s^2 | 60 FPS => 1/60 * a
        x_velocity = self.velocity * math.cos(self.angle)
        y_velocity = self.velocity * math.sin(self.angle)

        objects_angle = calculate_two_point_angle([self.x, self.y], [other_object.x, other_object.y])

        added_x_velocity = cos(objects_angle) * added_velocity
        added_y_velocity = sin(objects_angle) * added_velocity


        resultant_x_velocity = x_velocity + added_x_velocity
        resultant_y_velocity = y_velocity + added_y_velocity

        resultant_angle = calculate_by_distance_angle(resultant_x_velocity, resultant_y_velocity)
        resultant_velocity = sqrt(resultant_x_velocity ** 2 + resultant_y_velocity ** 2)
        self.velocity, self.angle = resultant_velocity, resultant_angle

    def change_position(self, fps):
        self.x = self.x + self.velocity * math.cos(self.angle) / fps
        self.y = self.y + self.velocity * math.sin(self.angle) / fps