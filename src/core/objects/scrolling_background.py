import math
from typing import Tuple

import pygame

from src.core.graphics import Drawable

class ScrollingBackground(Drawable):
    def __init__(self, pattern: pygame.Surface) -> None:
        self._pattern = pattern
        self._angle = 0
        self._speed = 50
        self._x = 0
        self._y = 0

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, value: float) -> None:
        self._angle = value

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        self._speed = value

    def process(self, delta: float) -> None:
        radians = math.radians(self._angle)
        self._x += math.cos(radians) * self._speed * delta
        self._y += math.sin(radians) * self._speed * delta
        
        if abs(self._x) > self._pattern.width:
            self._x = 0
        if abs(self._y) > self._pattern.height:
            self._y = 0

    def draw(self, surface: pygame.Surface) -> None:
        x_tiles = math.ceil(surface.width / self._pattern.width) + 1
        y_tiles = math.ceil(surface.height / self._pattern.height) + 1
        for x in range(-1, x_tiles):
            for y in range(-1, y_tiles):
                surface.blit(self._pattern, self._get_draw_position(x, y))

    def _get_draw_position(self, x: int, y: int) -> Tuple[int, int]:
        return (x * self._pattern.width + self._x, 
                y * self._pattern.height + self._y)
