import math
import pygame

class Background:
    def __init__(
        self, 
        surface: pygame.Surface, 
        direction: int = 0,
        speed: int = 5,
        special_flags: int = 0
    ) -> None:
        self._surface = surface
        self._position = [0, 0]
        self._direction = direction
        self._speed = speed
        self._special_flags = special_flags
    
    @property
    def surface(self) -> pygame.Surface:
        return self._surface
    
    @property
    def direction(self) -> int:
        return self._direction
    
    @property
    def speed(self) -> int:
        return self._speed

    @property
    def special_flags(self) -> int:
        return self._special_flags

    def update(self, delta: float) -> None:
        radians = math.radians(self.direction)
        self._position[0] += math.cos(radians) * self.speed * delta
        self._position[1] += math.sin(radians) * self.speed * delta
        if abs(self._position[0]) > self.surface.get_width():
            self._position[0] = 0
        if abs(self._position[1]) > self.surface.get_height():
            self._position[1] = 0
    
    def draw(self, surface: pygame.Surface) -> None:
        width = math.ceil(surface.get_width() / self.surface.get_width()) + 1
        height = math.ceil(surface.get_height() / self.surface.get_height()) + 1
        for x in range(-1, width):
            for y in range(-1, height):
                surface.blit(
                    self.surface, 
                    (
                        x * self.surface.get_width() + int(self._position[0]),
                        y * self.surface.get_height() + int(self._position[1])
                    ),
                    special_flags=self.special_flags
                )
