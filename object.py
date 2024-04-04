import scipy.constants
from pygame import Vector2
from scipy.constants import gravitational_constant
from math import cos, sin, sqrt

def calculate_cartesian_velocities(velocity, angle):
    x_velocity = velocity * cos(angle)
    y_velocity = velocity * sin(angle)
    return x_velocity, y_velocity

class SpaceObject:
    def __init__(self, x:int, y:int, mass:float, velocity: float, angle:float):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.angle = angle
        self.G = gravitational_constant

    def __str__(self):
        return f"Coordinates: {self.x}x{self.y}, the mass is equal to {self.mass}, the velocity is {self.velocity} and the angle is {self.angle}"
    def calculate_new_velocity(self, mass, distance, angle, fps):
        acceleration = (self.G * mass) / pow(distance, 2) # a = GM/R^2
        added_velocity = acceleration * (1/fps) # [a] = m/s^2 | 60 FPS => 1/60 * a
        x_added_velocity, y_added_velocity = calculate_cartesian_velocities(added_velocity, angle) # Calculate Velocities From Another Object
        x_current_velocity, y_current_velocity = calculate_cartesian_velocities(self.velocity, self.angle) # Calcute Velocities For This Object
        x_resultant_velocity = abs(x_added_velocity - x_current_velocity) # Resultant Velocity in X Axis
        y_resultant_velocity = abs(y_added_velocity - y_current_velocity) # Resultant Velocity in Y Axis
        resultant_velocity = sqrt(x_resultant_velocity ** 2 + y_resultant_velocity ** 2) # Pythagorean Triangle
        return resultant_velocity


    def get_cartesian_velocities(self):

