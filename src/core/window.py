from typing import Tuple

import pygame

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        self._flags = pygame.SCALED
        self._surface = pygame.display.set_mode((width, height), self._flags)
        self.set_title(title)

    def get_title(self) -> str:
        return pygame.display.get_caption()[0]

    def set_title(self, title: str) -> None:
        pygame.display.set_caption(title)

    def is_fullscreen(self) -> bool:
        return pygame.display.is_fullscreen()

    def set_fullscreen(self, fullscreen: bool) -> None:
        if fullscreen != self.is_fullscreen():
            self.toggle_fullscreen()

    def toggle_fullscreen(self) -> None:
        pygame.display.toggle_fullscreen()

    def get_mode(self) -> Tuple[int, int, int]:
        width, height = self._surface.get_size()
        return width, height, self._flags

    def get_surface(self) -> pygame.Surface:
        return self._surface

    def flip(self) -> None:
        pygame.display.flip()