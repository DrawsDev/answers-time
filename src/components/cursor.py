import math
import pygame
from pygame.math import Vector2
from src.settings import *
from src.components.sprite import Sprite

class Cursor(Sprite):
    def __init__(self, 
                 image: pygame.Surface, 
                 position: pygame.math.Vector2 = (0, 0), 
                 anchor: str = "topleft") -> None:
        super().__init__(image, position, anchor)

    def update(self, delta: float) -> None:
        mouse_pos = pygame.mouse.get_pos()
        ratio = Vector2(WINDOW_SIZE[0] / SURFACE_SIZE[0], WINDOW_SIZE[1] / SURFACE_SIZE[1])

        mouse_x = mouse_pos[0] / ratio.x
        mouse_y = mouse_pos[1] / ratio.y
        self.position = self.position + (Vector2(mouse_x, mouse_y) - self.position) * (5 * delta)

        wiggle_x = math.cos(pygame.time.get_ticks() / 500) * 2
        wiggle_y = math.sin(pygame.time.get_ticks() / 250) * 3
        self.anchor_offset = Vector2(13 + wiggle_x, -6 + wiggle_y)
