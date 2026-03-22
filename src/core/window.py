from typing import Tuple

import pygame


class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        self._size = (width, height)
        self._fullscreen = False
        self._display_index = 0
        self._surface = pygame.display.set_mode(self._size, pygame.RESIZABLE)
        self.set_title(title)

    def get_title(self) -> str:
        return pygame.display.get_caption()[0]

    def set_title(self, title: str) -> None:
        pygame.display.set_caption(title)

    def is_fullscreen(self) -> bool:
        return self._fullscreen

    def set_fullscreen(self, desktop: bool = True) -> None:
        if not self._fullscreen:
            self._fullscreen = True
            if not desktop:
                self._surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                self._surface = pygame.display.set_mode(
                    pygame.display.get_desktop_sizes()[self._display_index], pygame.NOFRAME
                )

    def is_windowed(self) -> bool:
        return not self._fullscreen

    def set_windowed(self) -> None:
        if self._fullscreen:
            self._fullscreen = False
            self._surface = pygame.display.set_mode(self._size, pygame.RESIZABLE)

    def get_display_index(self) -> int:
        return self._display_index

    def get_mode(self) -> Tuple[int, int]:
        width, height = self._surface.get_size()
        return width, height

    def get_surface(self) -> pygame.Surface:
        return self._surface

    def event(self, event: pygame.Event) -> None:
        if event.type == pygame.WINDOWDISPLAYCHANGED:
            self._display_index = event.display_index

    def flip(self) -> None:
        pygame.display.flip()
