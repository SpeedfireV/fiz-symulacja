from scipy.constants import gravitational_constant
from math import cos, sin, atan, sqrt


def calculate_cartesian_velocities(velocity, angle):
    x_velocity = velocity * cos(angle)
    y_velocity = velocity * sin(angle)
    return x_velocity, y_velocity


class SpaceObject:
    def __init__(self, x: int, y: int, mass: float, velocity: float, angle: float):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.angle = angle
        self.G = gravitational_constant

    def __str__(self):
        return (f"Coordinates: {self.x}x{self.y}, the mass is equal to {self.mass}, the velocity is {self.velocity}//"
                f" and the angle is {self.angle}")

    def calculate_new_velocity(self, mass: float, distance: float, angle: float, fps: int):
        acceleration = (self.G * mass) / pow(distance, 2)  # a = GM/R^2
        added_velocity = acceleration * (1 / fps)  # [a] = m/s^2 | 60 FPS => 1/60 * a
        x_added_velocity, y_added_velocity = calculate_cartesian_velocities(added_velocity,
                                                                            angle)  # Calculate Velocities From Another Object
        x_current_velocity, y_current_velocity = calculate_cartesian_velocities(self.velocity,
                                                                                self.angle)  # Calcute Velocities For This Object
        x_resultant_velocity = abs(x_added_velocity - x_current_velocity)  # Resultant Velocity in X Axis
        y_resultant_velocity = abs(y_added_velocity - y_current_velocity)  # Resultant Velocity in Y Axis
        resultant_velocity: float = sqrt(x_resultant_velocity ** 2 + y_resultant_velocity ** 2)  # Pythagorean Triangle
        tangens = y_resultant_velocity / x_resultant_velocity  # Calculate Tangens Value
        resultant_angle: float = atan(tangens)  # Calculate Angle In Radians
        return resultant_velocity, resultant_angle

    def change_position(self):  # TODO: Change position
        pass
