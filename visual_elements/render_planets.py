import pygame
from pygame import Color

from objects.object import SpaceObject


def render_planets(screen, objects: list[SpaceObject]):
    for object in objects:
        pygame.draw.circle(screen, Color(10, 190, 245), [object.x, object.y], radius=3)

